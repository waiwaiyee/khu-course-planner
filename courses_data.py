# ============================================================
# KHU 2025 Course Data — extracted from 교육과정 PDF
# Covers: 컴퓨터공학과 (CS), 인공지능학과 (AI), 소프트웨어융합학과 (SW)
# ============================================================

COURSES = [
    # ── MATH / 수학 기초 ─────────────────────────────────────
    {"id": "AMTH1001", "name": "미분방정식", "name_en": "Differential Equations",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공기초", "dept": ["CS", "SW"],
     "domain": ["math"], "prereqs": [],
     "career": ["AI_ML", "Data", "Backend"], "eng": False, "required": True},

    {"id": "AMTH1004", "name": "선형대수", "name_en": "Linear Algebra",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공기초", "dept": ["CS", "AI", "SW"],
     "domain": ["math", "ml"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": False, "required": True},

    {"id": "AMTH1009", "name": "미분적분학", "name_en": "Calculus",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공기초", "dept": ["CS", "AI", "SW"],
     "domain": ["math"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": False, "required": True},

    {"id": "EE211", "name": "확률및랜덤변수", "name_en": "Probability and Random Variables",
     "credits": 3, "diff": 3, "year": 2, "sem": [1, 2],
     "cat": "전공기초", "dept": ["CS", "AI"],
     "domain": ["math", "data"], "prereqs": ["AMTH1009"],
     "career": ["AI_ML", "Data"], "eng": False, "required": True},

    {"id": "AI1003", "name": "인공지능수학", "name_en": "Mathematics for AI",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공기초", "dept": ["AI"],
     "domain": ["math", "ml"], "prereqs": ["AMTH1009"],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    # ── 1학년 전공 기초 ──────────────────────────────────────
    {"id": "SWCON104", "name": "웹/파이선프로그래밍", "name_en": "Web/Python Programming",
     "credits": 3, "diff": 1, "year": 1, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["prog", "web"], "prereqs": [],
     "career": ["AI_ML", "Backend", "Fullstack", "Data", "Mobile"], "eng": True, "required": True},

    {"id": "CSE103", "name": "객체지향프로그래밍", "name_en": "Object-Oriented Programming",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["prog", "oop"], "prereqs": [],
     "career": ["AI_ML", "Backend", "Fullstack", "Mobile", "Security"], "eng": True, "required": True},

    {"id": "AI1001", "name": "인공지능개론", "name_en": "Introduction to AI",
     "credits": 3, "diff": 1, "year": 1, "sem": [1],
     "cat": "전공필수", "dept": ["AI"],
     "domain": ["ai", "intro"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    {"id": "AI1002", "name": "인공지능프로그래밍", "name_en": "AI Programming",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공필수", "dept": ["AI", "CS"],
     "domain": ["ai", "prog", "ml"], "prereqs": ["SWCON104"],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    {"id": "CSE104", "name": "실감미디어컴퓨팅기초", "name_en": "Immersive Media Computing Basics",
     "credits": 3, "diff": 1, "year": 1, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["media", "prog"], "prereqs": [],
     "career": ["Fullstack", "Mobile"], "eng": False, "required": False},

    {"id": "CSE201", "name": "이산구조", "name_en": "Discrete Structures",
     "credits": 3, "diff": 2, "year": 1, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["math", "cs_theory"], "prereqs": [],
     "career": ["AI_ML", "Backend", "Security"], "eng": False, "required": False},

    # ── 2학년 전공 ───────────────────────────────────────────
    {"id": "EE209", "name": "논리회로", "name_en": "Logic Circuit",
     "credits": 3, "diff": 2, "year": 2, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS"],
     "domain": ["hardware", "sys"], "prereqs": [],
     "career": ["Backend", "Security"], "eng": False, "required": True},

    {"id": "CSE203", "name": "컴퓨터구조", "name_en": "Computer Architecture",
     "credits": 3, "diff": 3, "year": 2, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS"],
     "domain": ["sys", "hardware"], "prereqs": ["EE209"],
     "career": ["Backend", "Security"], "eng": False, "required": True},

    {"id": "CSE204", "name": "자료구조", "name_en": "Data Structures",
     "credits": 3, "diff": 3, "year": 2, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["prog", "ds", "algo"], "prereqs": ["CSE103"],
     "career": ["AI_ML", "Backend", "Fullstack", "Data", "Security"], "eng": True, "required": True},

    {"id": "SWCON201", "name": "오픈소스SW개발방법및도구", "name_en": "Opensource SW Dev Methods & Tools",
     "credits": 3, "diff": 2, "year": 2, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "SW"],
     "domain": ["sw_eng", "tools"], "prereqs": [],
     "career": ["Backend", "Fullstack", "Mobile"], "eng": True, "required": True},

    {"id": "SWCON253", "name": "기계학습", "name_en": "Machine Learning",
     "credits": 3, "diff": 4, "year": 2, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["ai", "ml"], "prereqs": ["AMTH1004"],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    {"id": "CSE224", "name": "UI/UX프로그래밍", "name_en": "UI/UX Programming",
     "credits": 3, "diff": 2, "year": 2, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["web", "design"], "prereqs": [],
     "career": ["Fullstack", "Mobile"], "eng": False, "required": False},

    {"id": "SWCON103", "name": "디자인적사고", "name_en": "Design Thinking",
     "credits": 3, "diff": 1, "year": 2, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["design", "sw_eng"], "prereqs": [],
     "career": ["Fullstack", "Mobile", "Backend"], "eng": True, "required": False},

    {"id": "SWCON211", "name": "게임프로그래밍입문", "name_en": "Intro to Game Programming",
     "credits": 3, "diff": 2, "year": 2, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["game", "prog"], "prereqs": [],
     "career": ["Mobile", "Fullstack"], "eng": False, "required": False},

    {"id": "SWCON221", "name": "마이크로서비스프로그래밍", "name_en": "Microservice Programming",
     "credits": 3, "diff": 3, "year": 2, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["web", "backend", "cloud"], "prereqs": [],
     "career": ["Backend", "Fullstack"], "eng": True, "required": False},

    {"id": "EE210", "name": "신호와시스템", "name_en": "Signals and Systems",
     "credits": 3, "diff": 3, "year": 2, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["math", "hardware"], "prereqs": ["AMTH1009"],
     "career": ["AI_ML", "Data"], "eng": False, "required": False},

    # ── 3학년 전공필수 ───────────────────────────────────────
    {"id": "CSE301", "name": "운영체제", "name_en": "Operating Systems",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["sys", "os"], "prereqs": ["CSE204"],
     "career": ["Backend", "Security", "AI_ML"], "eng": True, "required": True},

    {"id": "CSE302", "name": "컴퓨터네트워크", "name_en": "Computer Networks",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS"],
     "domain": ["net", "sys"], "prereqs": [],
     "career": ["Backend", "Security", "Fullstack"], "eng": True, "required": True},

    {"id": "CSE304", "name": "알고리즘", "name_en": "Algorithms",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["algo", "cs_theory"], "prereqs": ["CSE204"],
     "career": ["AI_ML", "Backend", "Data", "Security"], "eng": True, "required": True},

    {"id": "CSE305", "name": "데이터베이스", "name_en": "Database",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["db", "data"], "prereqs": [],
     "career": ["Backend", "Fullstack", "Data", "AI_ML"], "eng": True, "required": True},

    {"id": "CSE327", "name": "소프트웨어공학", "name_en": "Software Engineering",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI", "SW"],
     "domain": ["sw_eng"], "prereqs": [],
     "career": ["Backend", "Fullstack", "Mobile"], "eng": False, "required": True},

    {"id": "CSE331", "name": "딥러닝", "name_en": "Deep Learning",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["AI", "CS"],
     "domain": ["ai", "ml", "dl"], "prereqs": ["SWCON253"],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    {"id": "CSE340", "name": "실전기계학습", "name_en": "Machine Learning Application",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["AI", "CS"],
     "domain": ["ai", "ml"], "prereqs": ["SWCON253"],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    {"id": "AI3001", "name": "고급딥러닝", "name_en": "Advanced Deep Learning",
     "credits": 3, "diff": 5, "year": 3, "sem": [1, 2],
     "cat": "전공필수", "dept": ["AI", "CS"],
     "domain": ["ai", "dl"], "prereqs": ["CSE331"],
     "career": ["AI_ML"], "eng": True, "required": True},

    {"id": "AI3002", "name": "인공지능과윤리", "name_en": "AI and Ethics",
     "credits": 3, "diff": 1, "year": 3, "sem": [1],
     "cat": "전공필수", "dept": ["AI"],
     "domain": ["ai", "ethics"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": True, "required": True},

    # ── 3학년 전공선택 ───────────────────────────────────────
    {"id": "CSE322", "name": "컴파일러", "name_en": "Compiler",
     "credits": 3, "diff": 4, "year": 3, "sem": [1],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["cs_theory", "prog"], "prereqs": [],
     "career": ["Backend", "Security"], "eng": False, "required": False},

    {"id": "CSE324", "name": "메타버스시스템", "name_en": "Metaverse Systems",
     "credits": 3, "diff": 3, "year": 3, "sem": [1],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["media", "game"], "prereqs": [],
     "career": ["Fullstack", "Mobile"], "eng": False, "required": False},

    {"id": "CSE328", "name": "프로그래밍언어론", "name_en": "Programming Languages",
     "credits": 3, "diff": 3, "year": 3, "sem": [1],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["cs_theory", "prog"], "prereqs": [],
     "career": ["Backend", "AI_ML"], "eng": False, "required": False},

    {"id": "CSE330", "name": "SW스타트업비즈니스", "name_en": "SW Startup Business",
     "credits": 3, "diff": 1, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["biz"], "prereqs": [],
     "career": ["Backend", "Fullstack", "Mobile", "AI_ML", "Data"], "eng": False, "required": False},

    {"id": "CSE332", "name": "리눅스시스템프로그래밍", "name_en": "Linux System Programming",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["sys", "os"], "prereqs": [],
     "career": ["Backend", "Security"], "eng": False, "required": False},

    {"id": "CSE335", "name": "클라우드컴퓨팅", "name_en": "Cloud Computing",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["cloud", "backend"], "prereqs": [],
     "career": ["Backend", "Fullstack", "Data"], "eng": True, "required": False},

    {"id": "CSE434", "name": "빅데이터프로그래밍", "name_en": "Big Data Programming",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["data", "ml"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": False, "required": False},

    {"id": "CSE443", "name": "AI네트워킹", "name_en": "AI Networking",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["ai", "net"], "prereqs": [],
     "career": ["AI_ML", "Backend"], "eng": True, "required": False},

    {"id": "SWCON302", "name": "최신기술콜로키움2", "name_en": "Latest Tech Colloquium 2",
     "credits": 2, "diff": 1, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["survey"], "prereqs": [],
     "career": ["AI_ML", "Backend", "Data", "Fullstack", "Security", "Mobile"], "eng": True, "required": False},

    {"id": "SWCON311", "name": "게임그래픽프로그래밍", "name_en": "Game Graphics Programming",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["game", "graphics"], "prereqs": [],
     "career": ["Mobile", "Fullstack"], "eng": False, "required": False},

    {"id": "SWCON313", "name": "가상/증강현실이론및실습", "name_en": "VR/AR Theory & Practice",
     "credits": 3, "diff": 3, "year": 3, "sem": [1],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["media", "game"], "prereqs": [],
     "career": ["Mobile", "Fullstack"], "eng": True, "required": False},

    {"id": "SWCON331", "name": "로봇프로그래밍", "name_en": "Robot Programming",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["ai", "iot"], "prereqs": [],
     "career": ["AI_ML"], "eng": False, "required": False},

    {"id": "SWCON366", "name": "3D데이터처리", "name_en": "3D Data Processing",
     "credits": 3, "diff": 3, "year": 3, "sem": [1],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["ai", "graphics"], "prereqs": [],
     "career": ["AI_ML", "Fullstack"], "eng": True, "required": False},

    {"id": "SWCON370", "name": "풀스택서비스프로그래밍", "name_en": "Full-Stack Service Programming",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["web", "backend", "fullstack"], "prereqs": [],
     "career": ["Fullstack", "Backend", "Mobile"], "eng": True, "required": False},

    {"id": "AI3003", "name": "자연언어학습", "name_en": "Natural Language Learning",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["AI"],
     "domain": ["ai", "nlp"], "prereqs": ["CSE331"],
     "career": ["AI_ML"], "eng": True, "required": False},

    {"id": "AI3004", "name": "빅데이터마이닝", "name_en": "Big Data Mining",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["AI", "CS"],
     "domain": ["ai", "data", "ml"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": True, "required": False},

    {"id": "AI3005", "name": "정보검색", "name_en": "Information Retrieval",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["AI"],
     "domain": ["ai", "nlp", "data"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": True, "required": False},

    {"id": "AI3006", "name": "지식표현및추론", "name_en": "Knowledge Representation & Reasoning",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["AI"],
     "domain": ["ai", "cs_theory"], "prereqs": [],
     "career": ["AI_ML"], "eng": True, "required": False},

    {"id": "AI3007", "name": "통계적학습이론", "name_en": "Statistical Learning Theory",
     "credits": 3, "diff": 5, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["AI"],
     "domain": ["math", "ml", "data"], "prereqs": ["SWCON253"],
     "career": ["AI_ML", "Data"], "eng": True, "required": False},

    {"id": "AI3008", "name": "설명및신뢰가능한AI", "name_en": "Explainable and Reliable AI",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["AI"],
     "domain": ["ai", "ml"], "prereqs": ["CSE331"],
     "career": ["AI_ML", "Data"], "eng": True, "required": False},

    {"id": "SWCON491", "name": "인공지능과게임프로그래밍", "name_en": "AI and Game Programming",
     "credits": 3, "diff": 3, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["ai", "game"], "prereqs": [],
     "career": ["AI_ML", "Mobile"], "eng": False, "required": False},

    {"id": "SWCON493", "name": "자연언어처리", "name_en": "Natural Language Processing",
     "credits": 3, "diff": 4, "year": 3, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["ai", "nlp"], "prereqs": ["CSE331"],
     "career": ["AI_ML"], "eng": True, "required": False},

    {"id": "SWCON495", "name": "강화학습", "name_en": "Reinforcement Learning",
     "credits": 3, "diff": 5, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI", "SW"],
     "domain": ["ai", "ml"], "prereqs": ["SWCON253"],
     "career": ["AI_ML"], "eng": True, "required": False},

    # ── 4학년 전공선택 ───────────────────────────────────────
    {"id": "CSE406", "name": "캡스톤디자인", "name_en": "Capstone Design",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공필수", "dept": ["CS", "AI"],
     "domain": ["project"], "prereqs": [],
     "career": ["AI_ML", "Backend", "Fullstack", "Data", "Security", "Mobile"], "eng": False, "required": True},

    {"id": "CSE423", "name": "정보보호", "name_en": "Information Security",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["security", "net"], "prereqs": [],
     "career": ["Security", "Backend"], "eng": True, "required": False},

    {"id": "CSE426", "name": "영상처리", "name_en": "Image Processing",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["ai", "cv"], "prereqs": [],
     "career": ["AI_ML"], "eng": True, "required": False},

    {"id": "CSE428", "name": "컴퓨터그래픽스", "name_en": "Computer Graphics",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["graphics", "ai"], "prereqs": [],
     "career": ["Mobile", "Fullstack", "AI_ML"], "eng": False, "required": False},

    {"id": "CSE436", "name": "빅데이터프로젝트", "name_en": "Big Data Project",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["data", "project"], "prereqs": ["CSE434"],
     "career": ["AI_ML", "Data"], "eng": False, "required": False},

    {"id": "CSE437", "name": "클라우드프로젝트", "name_en": "Cloud Project",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["cloud", "project"], "prereqs": ["CSE335"],
     "career": ["Backend", "Data", "Fullstack"], "eng": True, "required": False},

    {"id": "CSE438", "name": "최신기술콜로키움1", "name_en": "Latest Tech Colloquium 1",
     "credits": 2, "diff": 1, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["survey"], "prereqs": [],
     "career": ["AI_ML", "Backend", "Data", "Fullstack", "Security", "Mobile"], "eng": True, "required": False},

    {"id": "CSE439", "name": "AIoT디지털시스템", "name_en": "AIoT Digital Systems",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["iot", "hardware"], "prereqs": ["CSE203"],
     "career": ["Backend", "AI_ML"], "eng": False, "required": False},

    {"id": "CSE440", "name": "AIoT소프트웨어", "name_en": "AIoT Software",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["iot", "ai"], "prereqs": [],
     "career": ["Backend", "AI_ML"], "eng": False, "required": False},

    {"id": "CSE441", "name": "컴퓨터비젼", "name_en": "Computer Vision",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["ai", "cv"], "prereqs": [],
     "career": ["AI_ML"], "eng": True, "required": False},

    {"id": "CSE442", "name": "블록체인", "name_en": "Blockchain",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["blockchain", "security"], "prereqs": [],
     "career": ["Security", "Backend"], "eng": True, "required": False},

    {"id": "CSE444", "name": "AIoT네트워크", "name_en": "AIoT Network",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["net", "iot"], "prereqs": [],
     "career": ["Backend", "AI_ML"], "eng": False, "required": False},

    {"id": "CSE450", "name": "모바일/웹서비스프로그래밍", "name_en": "Mobile/Web Service Programming",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "AI"],
     "domain": ["mobile", "web", "fullstack"], "prereqs": [],
     "career": ["Mobile", "Fullstack"], "eng": True, "required": False},

    {"id": "CSE452", "name": "소프트웨어보안", "name_en": "Software Security",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["security", "prog"], "prereqs": [],
     "career": ["Security", "Backend"], "eng": True, "required": False},

    {"id": "CSE453", "name": "웹보안", "name_en": "Web Security",
     "credits": 3, "diff": 4, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS"],
     "domain": ["security", "web"], "prereqs": [],
     "career": ["Security", "Fullstack"], "eng": True, "required": False},

    {"id": "AI4003", "name": "졸업논문(인공지능)", "name_en": "Graduation Thesis (AI)",
     "credits": 0, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공필수", "dept": ["AI"],
     "domain": ["project"], "prereqs": [],
     "career": ["AI_ML"], "eng": False, "required": True},

    {"id": "AI4004", "name": "AI최신기술", "name_en": "Recent Advances in AI",
     "credits": 3, "diff": 3, "year": 4, "sem": [1],
     "cat": "전공선택", "dept": ["AI"],
     "domain": ["ai", "survey"], "prereqs": [],
     "career": ["AI_ML", "Data"], "eng": True, "required": False},

    {"id": "SWCON492", "name": "풀스택서비스네트워킹", "name_en": "Full-Stack Service Networking",
     "credits": 3, "diff": 3, "year": 4, "sem": [1, 2],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["web", "net", "fullstack"], "prereqs": [],
     "career": ["Fullstack", "Backend"], "eng": True, "required": False},

    {"id": "SWCON496", "name": "소프트웨어융합보안", "name_en": "SW Convergence Security",
     "credits": 3, "diff": 4, "year": 2, "sem": [2],
     "cat": "전공선택", "dept": ["CS", "SW"],
     "domain": ["security"], "prereqs": [],
     "career": ["Security"], "eng": False, "required": False},
]

# ── Career goal definitions ──────────────────────────────────
CAREER_GOALS = {
    "AI_ML":    {"label": "AI / Machine Learning Engineer",    "icon": "🤖"},
    "Data":     {"label": "Data Scientist",                    "icon": "📊"},
    "Backend":  {"label": "Backend Developer",                 "icon": "⚙️"},
    "Fullstack":{"label": "Full-Stack Developer",              "icon": "🌐"},
    "Security": {"label": "Cybersecurity Engineer",            "icon": "🔐"},
    "Mobile":   {"label": "Mobile App Developer",              "icon": "📱"},
}

# ── Department definitions ────────────────────────────────────
DEPARTMENTS = {
    "CS":  "컴퓨터공학과 (Computer Engineering)",
    "AI":  "인공지능학과 (Artificial Intelligence)",
    "SW":  "소프트웨어융합학과 (SW Convergence)",
}

# ── Graduation requirements per dept ─────────────────────────
GRAD_REQUIREMENTS = {
    "CS": {
        "total": 130,
        "전공기초": 12,
        "전공필수": 42,
        "전공선택": 15,
        "영어강좌": 3,    # 3 courses in English
    },
    "AI": {
        "total": 130,
        "전공기초": 12,
        "전공필수": 42,
        "전공선택": 27,
        "영어강좌": 3,
    },
    "SW": {
        "total": 130,
        "전공기초": 12,
        "전공필수": 30,
        "전공선택": 18,
        "영어강좌": 3,
    },
}
