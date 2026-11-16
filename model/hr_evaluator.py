# ==========================================
# HR Interview Evaluator
# ==========================================


# ==========================================
# Important Keywords for Each HR Question
# ==========================================

hr_keywords = {

    1: {
        "education": ["b.tech", "degree", "student", "engineering", "college"],
        "skills": ["python", "java", "coding", "programming", "machine learning", "ai", "technical"],
        "experience": ["project", "internship", "experience", "worked", "developed"],
        "goals": ["goal", "career", "future", "aim", "aspire"],
        "introduction": ["myself", "name", "from", "studying", "pursuing"]
    },

    2: {
        "communication": ["communication", "communicate", "speaking", "explain"],
        "teamwork": ["teamwork", "team", "collaborate", "together", "cooperation"],
        "problem solving": ["problem solving", "solve problems", "solution", "solve", "debug"],
        "leadership": ["leadership", "leader", "lead", "responsibility"],
        "learning": ["learning", "learn", "new skills", "improve", "adapt"]
    },

    3: {
        "improvement": ["improve", "improvement", "develop", "work on", "better"],
        "learning": ["learn", "learning", "new skill", "practice", "training"],
        "challenge": ["challenge", "difficult", "difficulty", "mistake", "failure"],
        "self-awareness": ["weakness", "strength", "aware", "understand", "recognize"]
    },

    4: {
        "skills": ["skill", "python", "java", "coding", "technical", "communication"],
        "experience": ["project", "internship", "experience", "worked", "developed"],
        "learning": ["learn", "learning", "improve", "adapt", "new technology"],
        "teamwork": ["team", "teamwork", "collaborate", "together"],
        "value": ["value", "contribute", "help", "benefit", "company", "organization"]
    },

    5: {
        "career": ["career", "job", "professional"],
        "growth": ["growth", "develop", "improve", "progress", "experience"],
        "skills": ["skills", "python", "java", "ai", "machine learning", "technical"],
        "leadership": ["leadership", "leader", "lead", "responsibility"],
        "goals": ["goal", "aim", "future", "achieve", "aspire"]
    }
}


# ==========================================
# Display Names
# ==========================================

concept_names = {

    "education": "education",

    "skills": "skills",

    "experience": "experience",

    "goals": "career goals",

    "introduction": "personal introduction",

    "communication": "communication",

    "teamwork": "teamwork",

    "problem solving": "problem solving",

    "leadership": "leadership",

    "learning": "willingness to learn",

    "improvement": "self-improvement",

    "challenge": "handling challenges",

    "self-awareness": "self-awareness",

    "value": "value you can bring to the company",

    "career": "career plans",

    "growth": "professional growth"
}


# ==========================================
# Evaluate HR Answer
# ==========================================

def evaluate_hr_answer(answer, question_number):

    student_answer = answer.lower().strip()

    keywords = hr_keywords[question_number]

    strengths = []

    weaknesses = []

    achieved_concepts = 0

    total_concepts = len(keywords)


    # ======================================
    # Check Important Concepts
    # ======================================

    for concept, word_list in keywords.items():

        found = False

        for word in word_list:

            if word in student_answer:

                found = True

                break


        if found:

            achieved_concepts += 1

            strengths.append(

                "Your answer covers "

                + concept_names[concept]

                + "."

            )

        else:

            weaknesses.append(

                "Consider discussing "

                + concept_names[concept]

                + "."

            )


    # ======================================
    # Answer Length
    # ======================================

    word_count = len(student_answer.split())


    if word_count >= 50:

        length_score = 2

        strengths.append(

            "Your answer provides good detail."

        )

    elif word_count >= 25:

        length_score = 1

    else:

        length_score = 0

        weaknesses.append(

            "Try to provide a more detailed answer."

        )


    # ======================================
    # Concept Score
    # Maximum = 8
    # ======================================

    concept_score = (

        achieved_concepts / total_concepts

    ) * 8


    # ======================================
    # Final Score
    # Maximum = 10
    # ======================================

    final_score = concept_score + length_score

    score = round(final_score)


    # Keep score between 0 and 10

    if score > 10:

        score = 10

    if score < 0:

        score = 0


    # ======================================
    # Feedback
    # ======================================

    if score >= 9:

        feedback = (

            "Excellent HR answer! Your response is "

            "relevant, detailed and well structured."

        )

    elif score >= 7:

        feedback = (

            "Good answer! You covered several important "

            "points. Add specific examples to make it stronger."

        )

    elif score >= 5:

        feedback = (

            "Fair attempt! Your answer contains some "

            "relevant points, but more detail is needed."

        )

    elif score >= 3:

        feedback = (

            "Your answer needs improvement. Try to explain "

            "your points clearly and include relevant examples."

        )

    else:

        feedback = (

            "Your answer is too brief or lacks relevant "

            "information. Try to explain your answer clearly."

        )


    # ======================================
    # Return Result
    # ======================================

    return (

        score,

        feedback,

        strengths,

        weaknesses

    )