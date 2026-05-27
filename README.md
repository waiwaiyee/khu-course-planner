# KHU AI Course Planner
**AI-Based Smart Course Recommendation System for Kyung Hee University Students**
Team 05 · La Min Eainn · May Sapal · Wai Wai Yee · 2025

---

## Quick Start (Run on Your Computer)

### Requirements
- Python 3.9 or higher
- pip (comes with Python)

### 1. Install dependencies
Open a terminal / command prompt in this folder and run:

```bash
pip install -r requirements.txt
```

### 2. Start the server

```bash
python app.py
```

### 3. Open in browser
Go to → **http://localhost:5000**

That's it! The website is now running on your computer.

---

## How to Deploy (Make it Public on the Internet)

### Option A — PythonAnywhere (free, easiest)
1. Sign up at https://www.pythonanywhere.com (free tier)
2. Upload all files via the Files tab
3. Create a new Web App → Flask → Python 3.11
4. Set source directory to `/home/<yourusername>/khu_planner`
5. WSGI file: `from app import app as application`
6. Reload → your site is live at `<yourusername>.pythonanywhere.com`

### Option B — Render (free tier, GitHub)
1. Push this folder to a GitHub repository
2. Go to https://render.com → New Web Service
3. Connect your repo, set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Deploy → free public URL

### Option C — Local network (share with classmates)
Run with:
```bash
python app.py --host 0.0.0.0
```
Share your IP address (e.g. http://192.168.1.5:5000) with anyone on the same WiFi.

---

## Project Structure

```
khu_planner/
├── app.py              ← Flask server (AI engine + API)
├── courses_data.py     ← 2025 KHU curriculum data (from PDF)
├── requirements.txt    ← Python packages
├── README.md           ← This file
├── templates/
│   └── index.html      ← Main web page
└── static/
    ├── css/style.css   ← Styles
    └── js/app.js       ← Frontend logic
```

## AI Methodology (from Proposal)

| Method | Implementation |
|---|---|
| Content-Based Filtering | Cosine similarity between student domain profile and course domain vectors |
| Prerequisite Graph Validation | Each course carries a `prereqs` list; only courses with all prereqs met are shown |
| Workload Scoring | Average difficulty score of selected courses → Balanced / Moderate / Heavy |
| International Support | English-medium courses flagged and score-boosted for international students |

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Main web interface |
| `/api/courses?dept=CS` | GET | All courses for a department |
| `/api/recommend` | POST | Run recommendation engine |
| `/api/prereq_check` | POST | Check if a single course's prereqs are met |
