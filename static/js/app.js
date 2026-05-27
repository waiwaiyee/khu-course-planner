/* ── KHU AI Course Planner · app.js ────────────────────────── */

let allCourses   = [];
let selectedIds  = new Set();
let currentFilter = "all";
let currentCareer = "AI_ML";

// ── Initialise ───────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("dept").addEventListener("change", loadCourses);
  loadCourses();
});

async function loadCourses() {
  const dept = document.getElementById("dept").value;
  selectedIds.clear();
  const res  = await fetch(`/api/courses?dept=${dept}`);
  allCourses  = await res.json();
  renderCourseGrid(currentFilter);
}

// ── Step navigation ──────────────────────────────────────────
function goStep(n) {
  document.querySelectorAll(".step-panel").forEach((el, i) => {
    el.classList.toggle("active", i + 1 === n);
  });
  [1, 2, 3].forEach(i => {
    const tab = document.getElementById("tab" + i);
    tab.classList.remove("active", "done");
    if (i === n) tab.classList.add("active");
    else if (i < n) tab.classList.add("done");
  });
  document.getElementById("progressBar").style.width = (n / 3 * 100) + "%";
  if (n === 2) renderCourseGrid(currentFilter);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── Career selection ─────────────────────────────────────────
function selectCareer(el) {
  document.querySelectorAll(".career-card").forEach(c => c.classList.remove("selected"));
  el.classList.add("selected");
  currentCareer = el.dataset.career;
}

// ── Course grid ──────────────────────────────────────────────
function filterCat(cat, btn) {
  currentFilter = cat;
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  renderCourseGrid(cat);
}

function renderCourseGrid(filter) {
  const grid = document.getElementById("completedGrid");
  const dept = document.getElementById("dept").value;

  const visible = allCourses.filter(c => filter === "all" || c.cat === filter);

  grid.innerHTML = visible.map(c => {
    const checked = selectedIds.has(c.id);
    const tagCat  = c.cat === "전공필수" ? "tag-필수"
                  : c.cat === "전공기초" ? "tag-기초" : "tag-선택";
    return `
      <div class="course-card ${checked ? "checked" : ""}" onclick="toggleCourse('${c.id}', this)">
        <input type="checkbox" id="chk_${c.id}" ${checked ? "checked" : ""}
               onchange="toggleCourse('${c.id}', this.parentElement)" onclick="event.stopPropagation()">
        <div>
          <div class="cc-name">${c.name}</div>
          <div class="cc-id">${c.id} · ${c.credits}cr · Y${c.year}</div>
          <div class="cc-tags">
            <span class="tag ${tagCat}">${c.cat}</span>
            ${c.eng ? '<span class="tag tag-eng">English</span>' : ""}
          </div>
        </div>
      </div>`;
  }).join("");

  updateSelectedCount();
}

function toggleCourse(id, el) {
  const chk = document.getElementById("chk_" + id);
  if (selectedIds.has(id)) {
    selectedIds.delete(id);
    el.classList.remove("checked");
    if (chk) chk.checked = false;
  } else {
    selectedIds.add(id);
    el.classList.add("checked");
    if (chk) chk.checked = true;
  }
  updateSelectedCount();
}

function updateSelectedCount() {
  const n = selectedIds.size;
  document.getElementById("selectedCount").textContent =
    n === 0 ? "No courses selected" : `${n} course${n > 1 ? "s" : ""} selected`;
}

// ── Recommend ────────────────────────────────────────────────
async function runRecommendation() {
  const dept   = document.getElementById("dept").value;
  const year   = parseInt(document.getElementById("year").value);
  const sem    = parseInt(document.getElementById("semester").value);
  const isIntl = document.getElementById("stype").value === "international";

  const res  = await fetch("/api/recommend", {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      dept, year, career: currentCareer,
      completed: [...selectedIds],
      international: isIntl, semester: sem,
    }),
  });
  const data = await res.json();
  renderResults(data, dept, year);
  goStep(3);
}

// ── Render results ────────────────────────────────────────────
function renderResults(data, dept, year) {
  const { recommendations: recs, graduation: grad, workload: wl } = data;

  // Summary line
  document.getElementById("recSummaryLine").textContent =
    `${dept} · Year ${year} · ${selectedIds.size} courses completed · Career: ${currentCareer}`;

  // Metric cards
  const totalCr   = recs.slice(0, 6).reduce((s, c) => s + c.credits, 0);
  document.getElementById("summaryCards").innerHTML = `
    <div class="metric-card">
      <div class="metric-label">Recommendations</div>
      <div class="metric-value">${recs.length}</div>
      <div class="metric-sub">eligible courses</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Semester Credits</div>
      <div class="metric-value">${totalCr}</div>
      <div class="metric-sub">top 6 picks</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Completed</div>
      <div class="metric-value">${selectedIds.size}</div>
      <div class="metric-sub">courses done</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Req. Progress</div>
      <div class="metric-value">${grad.req_courses_done}<span style="font-size:14px;color:var(--text-3)">/${grad.req_courses_total}</span></div>
      <div class="metric-sub">required courses</div>
    </div>`;

  // Workload
  const wlClass = wl.level === "balanced" ? "wl-balanced"
                : wl.level === "moderate" ? "wl-moderate" : "wl-heavy";
  const wlIcon  = wl.level === "balanced" ? "✅"
                : wl.level === "moderate" ? "⚡" : "⚠️";
  const wlMsg   = wl.level === "balanced"
    ? "Balanced workload — good semester plan."
    : wl.level === "moderate"
    ? "Moderate workload — manage your time carefully."
    : "Heavy workload detected! Consider replacing a high-difficulty course.";
  document.getElementById("workloadAlert").innerHTML = `
    <div class="workload-box ${wlClass}">
      <span class="wl-icon">${wlIcon}</span>
      <span>${wlMsg} Avg difficulty: ${wl.avg_diff}/5</span>
    </div>`;

  // Graduation tracker
  const rows = [
    { name: "전공기초 (Foundation)", done: grad.foundation_credits_done, need: grad.foundation_credits_needed, unit: "cr" },
    { name: "전공필수 (Core Required)", done: grad.req_credits_done,     need: grad.req_credits_needed,        unit: "cr" },
    { name: "전공선택 (Electives)",     done: grad.elective_credits_done, need: grad.elective_credits_needed,   unit: "cr" },
    { name: "English Courses",          done: grad.english_done,          need: grad.english_needed,             unit: "courses" },
  ];
  document.getElementById("gradTracker").innerHTML = rows.map(r => {
    const pct  = Math.min(100, Math.round(r.done / r.need * 100));
    const ok   = r.done >= r.need;
    return `
      <div class="grad-row">
        <div class="grad-name">${r.name}</div>
        <div class="grad-right">
          <div class="grad-prog">
            <div class="grad-prog-fill" style="width:${pct}%"></div>
          </div>
          <div class="grad-val ${ok ? "ok" : "warn"}">
            ${r.done}/${r.need} ${r.unit}
            ${ok ? '<span class="done-check">✓</span>' : ""}
          </div>
        </div>
      </div>`;
  }).join("");

  // Prereq warnings
  const missingPrereqs = [];
  recs.slice(0, 6).forEach(c => {
    const missing = c.prereqs.filter(p => !selectedIds.has(p));
    if (missing.length) missingPrereqs.push({ name: c.name, missing });
  });
  document.getElementById("prereqWarnings").innerHTML = missingPrereqs.length
    ? missingPrereqs.map(w =>
        `<div class="prereq-warn">⚠ <strong>${w.name}</strong> — not yet recommended (unmet prereqs: ${w.missing.join(", ")})</div>`
      ).join("")
    : "";

  // Recommendation cards
  document.getElementById("recList").innerHTML = recs.slice(0, 6).map((c, i) => {
    const rankClass = i === 0 ? "r1" : i === 1 ? "r2" : i === 2 ? "r3" : "";
    const pct       = Math.round(c.score * 100);
    const dots      = [1,2,3,4,5].map(d =>
      `<span class="dot ${d <= c.diff ? "filled" : ""}"></span>`).join("");
    return `
      <div class="rec-card ${i < 3 ? "top" : ""}">
        <div class="rec-rank ${rankClass}">${i + 1}</div>
        <div class="rec-body">
          <div class="rec-title">${c.name}</div>
          <div class="rec-title-en">${c.name_en}</div>
          <div class="rec-meta">
            ${c.id} · ${c.credits} credits · Year ${c.year}
            · <span title="Difficulty">${c.cat}</span>
            · Difficulty <span class="diff-dots">${dots}</span>
          </div>
          <div class="rec-tags">
            ${c.career.includes(currentCareer) ? '<span class="pill pill-career">Career match</span>' : ""}
            ${c.cat === "전공필수" ? '<span class="pill pill-req">전공필수</span>' : ""}
            ${c.eng ? '<span class="pill pill-eng">English medium</span>' : ""}
            ${c.prereqs.length === 0 ? '<span class="pill pill-nopreq">No prereqs</span>' :
              `<span class="pill">Prereqs: ${c.prereqs.join(", ")}</span>`}
          </div>
          <div class="rec-score-row">
            <span class="score-label">Match score</span>
            <div class="score-bar-bg">
              <div class="score-bar-fill" style="width:${pct}%"></div>
            </div>
            <span class="score-pct">${pct}%</span>
          </div>
        </div>
      </div>`;
  }).join("") || `<p style="color:var(--text-3);font-size:14px;text-align:center;padding:2rem">
    No eligible courses found. Try adding more completed courses on the previous step.</p>`;

  // All eligible
  document.getElementById("eligibleList").innerHTML = recs.slice(6).map(c => `
    <div class="elig-card">
      <div class="elig-name">${c.name}</div>
      <div class="elig-id">${c.id} · ${c.credits}cr · ${c.cat}</div>
    </div>`).join("") || `<p style="padding:12px;color:var(--text-3);font-size:13px;">
      All eligible courses are already listed above.</p>`;
}
