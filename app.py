"""
KHU AI Course Planner — Flask backend
Run: python app.py  →  http://localhost:5000
"""
from flask import Flask, render_template, request, jsonify
import json, math
from courses_data import COURSES, CAREER_GOALS, DEPARTMENTS, GRAD_REQUIREMENTS

app = Flask(__name__)

# ── helpers ──────────────────────────────────────────────────
def cosine_sim(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot  = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    mag_a = math.sqrt(sum(v**2 for v in a.values()))
    mag_b = math.sqrt(sum(v**2 for v in b.values()))
    if not mag_a or not mag_b:
        return 0.0
    return dot / (mag_a * mag_b)

def build_profile(completed_ids):
    profile = {}
    for c in COURSES:
        if c["id"] in completed_ids:
            for d in c["domain"]:
                profile[d] = profile.get(d, 0) + 1
    return profile

def prereqs_met(course, completed_ids):
    return all(p in completed_ids for p in course["prereqs"])

def recommend(dept, year, career, completed_ids, is_intl, max_results=8):
    profile = build_profile(completed_ids)
    results = []
    for c in COURSES:
        if c["id"] in completed_ids:
            continue
        if dept not in c["dept"]:
            continue
        if not prereqs_met(c, completed_ids):
            continue
        if c["year"] > year + 1:          # don't suggest courses too far ahead
            continue

        c_vec = {d: 1 for d in c["domain"]}
        score = cosine_sim(profile, c_vec) * 0.45
        if career in c.get("career", []):
            score += 0.30
        if c["cat"] == "전공필수":
            score += 0.15
        if is_intl and c["eng"]:
            score += 0.10
        if c["diff"] > year + 1:
            score -= 0.15

        results.append({**c, "score": round(score, 3)})

    results.sort(key=lambda x: -x["score"])
    return results[:max_results]

def grad_analysis(dept, completed_ids):
    req = GRAD_REQUIREMENTS.get(dept, {})
    dept_courses = [c for c in COURSES if dept in c["dept"]]
    done = [c for c in dept_courses if c["id"] in completed_ids]

    completed_credits  = sum(c["credits"] for c in done)
    required_done      = [c for c in done if c["cat"] == "전공필수"]
    required_total     = [c for c in dept_courses if c["cat"] == "전공필수"]
    elective_done      = [c for c in done if c["cat"] == "전공선택"]
    foundation_done    = [c for c in done if c["cat"] == "전공기초"]
    english_done       = [c for c in done if c["eng"]]

    return {
        "completed_credits":  completed_credits,
        "total_required":     req.get("total", 130),
        "req_courses_done":   len(required_done),
        "req_courses_total":  len(required_total),
        "req_credits_done":   sum(c["credits"] for c in required_done),
        "req_credits_needed": req.get("전공필수", 42),
        "elective_credits_done": sum(c["credits"] for c in elective_done),
        "elective_credits_needed": req.get("전공선택", 15),
        "foundation_credits_done": sum(c["credits"] for c in foundation_done),
        "foundation_credits_needed": req.get("전공기초", 12),
        "english_done":       len(english_done),
        "english_needed":     req.get("영어강좌", 3),
    }

def workload(picks):
    if not picks:
        return "unknown", 0
    avg = sum(p["diff"] for p in picks) / len(picks)
    total_cr = sum(p["credits"] for p in picks)
    if avg < 2.5:
        level = "balanced"
    elif avg < 3.5:
        level = "moderate"
    else:
        level = "heavy"
    return level, round(avg, 1)

# ── routes ───────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html",
                           departments=DEPARTMENTS,
                           career_goals=CAREER_GOALS)

@app.route("/api/courses")
def api_courses():
    dept = request.args.get("dept", "CS")
    return jsonify([c for c in COURSES if dept in c["dept"]])

@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    data         = request.json
    dept         = data.get("dept", "CS")
    year         = int(data.get("year", 2))
    career       = data.get("career", "Backend")
    completed    = set(data.get("completed", []))
    is_intl      = data.get("international", False)

    recs   = recommend(dept, year, career, completed, is_intl)
    grad   = grad_analysis(dept, completed)
    wl_lv, wl_avg = workload(recs[:6])

    return jsonify({
        "recommendations": recs,
        "graduation":      grad,
        "workload":        {"level": wl_lv, "avg_diff": wl_avg},
    })

@app.route("/api/prereq_check", methods=["POST"])
def api_prereq_check():
    data      = request.json
    course_id = data.get("course_id")
    completed = set(data.get("completed", []))
    course    = next((c for c in COURSES if c["id"] == course_id), None)
    if not course:
        return jsonify({"ok": False, "missing": []})
    missing = [p for p in course["prereqs"] if p not in completed]
    missing_names = []
    for pid in missing:
        pc = next((c for c in COURSES if c["id"] == pid), None)
        if pc:
            missing_names.append({"id": pid, "name": pc["name"]})
    return jsonify({"ok": len(missing) == 0, "missing": missing_names})

if __name__ == "__main__":
    print("\n  KHU AI Course Planner")
    print("  Running at → http://localhost:5000\n")
    app.run(debug=True, port=5000)
