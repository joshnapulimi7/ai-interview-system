from flask import Flask, render_template, request, session

from model.evaluator import evaluate_answer
from model.hr_evaluator import evaluate_hr_answer
from model.coding_evaluator import evaluate_coding_answer
from database import (
    save_result,
    get_results,
    get_dashboard_stats,
    get_performance_data
)


# ==========================================
# Flask Application
# ==========================================

app = Flask(__name__)

app.secret_key = "ai_interview_secret_key"


# ==========================================
# Technical Interview Questions
# ==========================================

questions = [

    "What is Python?",

    "What are the advantages of Python?",

    "What is the difference between a list and a tuple?"

]


# ==========================================
# HR Interview Questions
# ==========================================

hr_questions = [

    "Tell me about yourself.",

    "What are your strengths?",

    "What is your weakness?",

    "Why should we hire you?",

    "Where do you see yourself in 5 years?"

]

# ==========================================
# Coding Interview Questions
# ==========================================

coding_questions = [

    {
        "question": "Write a Python program to check whether a number is even or odd.",
        "language": "Python"
    },

    {
        "question": "Write a Python program to find the largest of two numbers.",
        "language": "Python"
    },

    {
        "question": "Write a Python program to calculate the factorial of a number.",
        "language": "Python"
    }

]

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Technical Interview
# ==========================================

@app.route("/technical")
def technical():

    session["question_index"] = 0

    session["answers"] = []

    session["scores"] = []

    session["feedbacks"] = []

    session["strengths"] = []

    session["weaknesses"] = []

    return render_template(
        "technical.html",
        question=questions[0],
        question_number=1
    )


# ==========================================
# Submit Technical Interview Answer
# ==========================================

@app.route("/submit-answer", methods=["POST"])
def submit_answer():

    answer = request.form["answer"]

    question_index = session["question_index"]


    # ======================================
    # Evaluate Answer
    # ======================================

    score, feedback, strengths, weaknesses = evaluate_answer(

        answer,

        question_index + 1

    )


    # ======================================
    # Store Answer Details
    # ======================================

    session["answers"].append(answer)

    session["scores"].append(score)

    session["feedbacks"].append(feedback)

    session["strengths"].append(strengths)

    session["weaknesses"].append(weaknesses)


    # ======================================
    # Move to Next Question
    # ======================================

    session["question_index"] = question_index + 1


    # ======================================
    # Check Remaining Questions
    # ======================================

    if session["question_index"] < len(questions):

        next_question = questions[
            session["question_index"]
        ]

        return render_template(

            "technical.html",

            question=next_question,

            question_number=session["question_index"] + 1

        )


    # ======================================
    # Calculate Final Score
    # ======================================

    total_score = sum(session["scores"])

    maximum_score = len(questions) * 10

    percentage = (

        total_score / maximum_score

    ) * 100


    # ======================================
    # Determine Performance
    # ======================================

    if percentage >= 80:

        performance = "Excellent"

    elif percentage >= 60:

        performance = "Good"

    elif percentage >= 40:

        performance = "Average"

    else:

        performance = "Needs Improvement"


    # ======================================
    # Save Technical Result
    # ======================================

    save_result(

        "Technical",

        total_score,

        maximum_score,

        percentage,

        performance

    )


    # ======================================
    # Show Technical Result
    # ======================================

    return render_template(

        "result.html",

        answers=session["answers"],

        scores=session["scores"],

        feedbacks=session["feedbacks"],

        strengths=session["strengths"],

        weaknesses=session["weaknesses"],

        total_score=total_score,

        maximum_score=maximum_score,

        percentage=percentage,

        performance=performance

    )


# ==========================================
# HR Interview
# ==========================================

@app.route("/hr")
def hr():

    session["hr_question_index"] = 0

    session["hr_answers"] = []

    session["hr_scores"] = []

    session["hr_feedbacks"] = []

    session["hr_strengths"] = []

    session["hr_weaknesses"] = []

    return render_template(

        "hr.html",

        question=hr_questions[0],

        question_number=1

    )


# ==========================================
# Submit HR Interview Answer
# ==========================================

@app.route("/submit-hr-answer", methods=["POST"])
def submit_hr_answer():

    answer = request.form["answer"]

    question_index = session["hr_question_index"]


    # ======================================
    # Evaluate HR Answer
    # ======================================

    score, feedback, strengths, weaknesses = evaluate_hr_answer(

        answer,

        question_index + 1

    )


    # ======================================
    # Store Answer
    # ======================================

    session["hr_answers"].append(answer)

    session["hr_scores"].append(score)

    session["hr_feedbacks"].append(feedback)


    # ======================================
    # Store Strengths
    # ======================================

    if "hr_strengths" not in session:

        session["hr_strengths"] = []


    session["hr_strengths"].append(strengths)


    # ======================================
    # Store Weaknesses
    # ======================================

    if "hr_weaknesses" not in session:

        session["hr_weaknesses"] = []


    session["hr_weaknesses"].append(weaknesses)


    # ======================================
    # Move to Next Question
    # ======================================

    session["hr_question_index"] = question_index + 1


    # ======================================
    # Check Remaining Questions
    # ======================================

    if session["hr_question_index"] < len(hr_questions):

        next_question = hr_questions[

            session["hr_question_index"]

        ]

        return render_template(

            "hr.html",

            question=next_question,

            question_number=session["hr_question_index"] + 1

        )


    # ======================================
    # Calculate Final HR Score
    # ======================================

    total_score = sum(session["hr_scores"])

    maximum_score = len(hr_questions) * 10

    percentage = (

        total_score / maximum_score

    ) * 100


    # ======================================
    # Determine Performance
    # ======================================

    if percentage >= 80:

        performance = "Excellent"

    elif percentage >= 60:

        performance = "Good"

    elif percentage >= 40:

        performance = "Average"

    else:

        performance = "Needs Improvement"


    # ======================================
    # Save HR Result
    # ======================================

    save_result(

        "HR",

        total_score,

        maximum_score,

        percentage,

        performance

    )


    # ======================================
    # Show HR Result
    # ==========================================

    return render_template(

        "hr_result.html",

        answers=session["hr_answers"],

        scores=session["hr_scores"],

        feedbacks=session["hr_feedbacks"],

        strengths=session["hr_strengths"],

        weaknesses=session["hr_weaknesses"],

        total_score=total_score,

        maximum_score=maximum_score,

        percentage=percentage,

        performance=performance

    )


# ==========================================
# Coding Interview
# ==========================================

@app.route("/coding")
def coding():

    session["coding_question_index"] = 0

    session["coding_answers"] = []

    session["coding_scores"] = []

    session["coding_feedbacks"] = []
    session["coding_strengths"] = []
    session["coding_weaknesses"] = []


    return render_template(

        "coding.html",

        question=coding_questions[0]["question"],

        language=coding_questions[0]["language"],

        question_number=1,

        total_questions=len(coding_questions)

    )

# ==========================================
# Interview History
# ==========================================

@app.route("/history")
def history():

    results = get_results()

    return render_template(

        "history.html",

        results=results

    )


# ==========================================
# Dashboard
# ==========================================

@app.route("/dashboard")
def dashboard():

    total_interviews, average_score, best_score = get_dashboard_stats()

    performance_data = get_performance_data()

    return render_template(

        "dashboard.html",

        total_interviews=total_interviews,

        average_score=average_score,

        best_score=best_score,

        performance_data=performance_data

    )
# ==========================================
# Submit Coding Interview Answer
# ==========================================

@app.route("/submit-coding-answer", methods=["POST"])
def submit_coding_answer():

    code = request.form["code"]

    question_index = session["coding_question_index"]


    # AI Coding Evaluation
    score, feedback, strengths, weaknesses = evaluate_coding_answer(
    code,
    question_index + 1
)

    # ======================================
    # Store Coding Answer
    # ======================================

    session["coding_answers"].append(code)

    session["coding_scores"].append(score)

    session["coding_feedbacks"].append(feedback)


    # ======================================
    # Move to Next Question
    # ======================================

    session["coding_question_index"] = question_index + 1


    # ======================================
    # Check Remaining Questions
    # ======================================

    if session["coding_question_index"] < len(coding_questions):

        next_question = coding_questions[
            session["coding_question_index"]
        ]

        return render_template(

            "coding.html",

            question=next_question["question"],

            language=next_question["language"],

            question_number=session["coding_question_index"] + 1,

            total_questions=len(coding_questions)

        )


    # ======================================
    # Calculate Final Score
    # ======================================

    total_score = sum(session["coding_scores"])

    maximum_score = len(coding_questions) * 10

    percentage = (

        total_score / maximum_score

    ) * 100


    # ======================================
    # Performance
    # ======================================

    if percentage >= 80:

        performance = "Excellent"

    elif percentage >= 60:

        performance = "Good"

    elif percentage >= 40:

        performance = "Average"

    else:

        performance = "Needs Improvement"


    # ======================================
    # Save Coding Result
    # ======================================

    save_result(

        "Coding",

        total_score,

        maximum_score,

        percentage,

        performance

    )


    # ======================================
    # Show Result
    # ======================================

    return render_template(

        "coding_result.html",

        answers=session["coding_answers"],

        scores=session["coding_scores"],

        feedbacks=session["coding_feedbacks"],

        total_score=total_score,

        maximum_score=maximum_score,

        percentage=percentage,

        performance=performance

    )

# ==========================================
# Run Flask Application
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)