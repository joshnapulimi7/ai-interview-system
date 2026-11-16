# AI Interview System 🎯

**AI Interview System** is a full-stack mock interview preparation web application built with Python, Flask, and SQLite. It simulates real-world Technical, Coding, and HR interview rounds, evaluates candidate responses using AI/NLP evaluators, and tracks performance history on an interactive dashboard.

## ✨ Key Features
- **Multi-Round Interview Simulation:** Dedicated modules for Technical (`technical.html`), Coding (`coding.html`), and HR (`hr.html`) interview rounds.
- **Automated AI Evaluation:** Evaluates coding logic, technical accuracy, and HR behavioral answers using specialized evaluators (`coding_evaluator.py`, `evaluator.py`, `hr_evaluator.py`).
- **Performance Dashboard & History:** Tracks past interview scores, detailed feedback, and progress over time (`dashboard.html`, `history.html`).
- **Persistent Storage:** Stores user attempts, questions, and evaluation results using SQLite (`database.py`).

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite (`interview.db`)
- **Frontend:** HTML5, CSS3, JavaScript (`templates/`, `static/`)

## 📂 Project Structure
```text
AI_Interview_System/
├── app.py                     # Main Flask application entry point
├── database.py                # SQLite database setup and queries
├── requirements.txt           # Project dependencies
├── model/
│   ├── coding_evaluator.py    # Coding round evaluation logic
│   ├── evaluator.py           # Technical round evaluation logic
│   └── hr_evaluator.py        # HR behavioral evaluation logic
├── static/
│   ├── css/style.css          # Application styling
│   └── js/script.js           # Client-side interactivity
└── templates/
    ├── index.html             # Landing page
    ├── dashboard.html         # User analytics dashboard
    ├── interview.html         # Interview mode selection
    ├── technical.html         # Technical round interface
    ├── coding.html            # Coding round interface
    ├── hr.html                # HR round interface
    ├── result.html            # Technical evaluation results
    ├── coding_result.html     # Coding evaluation results
    ├── hr_result.html         # HR evaluation results
    └── history.html           # Past interview logs