from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# Reference Answers
# ==========================================

reference_answers = {

    1: """
    Python is a high-level interpreted programming language.
    It is easy to learn and has simple readable syntax.
    """,

    2: """
    Python is easy to learn and has readable syntax.
    It provides many libraries and frameworks.
    Python is portable, open-source, and widely used.
    """,

    3: """
    A list is mutable, while a tuple is immutable.
    Lists are commonly written using square brackets.
    Tuples are commonly written using parentheses.
    """
}


# ==========================================
# Important Concepts
# ==========================================

concepts = {

    1: {
        "high-level": 3,
        "interpreted": 3,
        "programming language": 4
    },

    2: {
        "easy to learn": 2,
        "readable": 2,
        "libraries": 2,
        "portable": 2,
        "open-source": 2
    },

    3: {
        "mutable": 3,
        "immutable": 3,
        "square brackets": 2,
        "parentheses": 2
    }
}


# ==========================================
# TF-IDF Similarity
# ==========================================

def calculate_similarity(student_answer, reference_answer):

    documents = [
        reference_answer,
        student_answer
    ]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return similarity


# ==========================================
# Evaluate Answer
# ==========================================

def evaluate_answer(answer, question_number):

    student_answer = answer.lower()

    reference_answer = reference_answers[question_number]

    question_concepts = concepts[question_number]


    # ======================================
    # 1. Calculate TF-IDF Similarity
    # ======================================

    similarity = calculate_similarity(
        student_answer,
        reference_answer
    )

    similarity_percentage = similarity * 100


    # ======================================
    # 2. Detect Concepts
    # ======================================

    strengths = []
    weaknesses = []

    total_concept_weight = sum(
        question_concepts.values()
    )

    achieved_concept_weight = 0


    for concept, weight in question_concepts.items():

        if concept in student_answer:

            achieved_concept_weight += weight

            strengths.append(
                "You correctly explained: " + concept
            )

        else:

            weaknesses.append(
                "Try to explain the concept: " + concept
            )


    # ======================================
    # 3. Concept Coverage
    # ======================================

    concept_percentage = (
        achieved_concept_weight /
        total_concept_weight
    ) * 100


    concept_score = (
        achieved_concept_weight /
        total_concept_weight
    ) * 10


    # ======================================
    # 4. Hybrid Score
    # ======================================

    # 70% concept coverage
    # 30% NLP similarity

    final_score = (
        (concept_score * 0.70) +
        (similarity * 10 * 0.30)
    )


    score = round(final_score)


    # Keep score between 0 and 10

    if score > 10:
        score = 10

    if score < 0:
        score = 0


    # ======================================
    # 5. Feedback
    # ======================================

    if score >= 9:

        feedback = (
            "Outstanding answer! You covered almost "
            "all important concepts accurately."
        )

    elif score >= 8:

        feedback = (
            "Excellent answer! You covered most of "
            "the important concepts clearly."
        )

    elif score >= 6:

        feedback = (
            "Good answer! You covered several important "
            "concepts, but some details can be improved."
        )

    elif score >= 4:

        feedback = (
            "Fair attempt! Your answer contains some "
            "relevant concepts, but more explanation is needed."
        )

    else:

        feedback = (
            "Your answer needs improvement. "
            "Try to explain the important concepts clearly."
        )


    # ======================================
    # 6. Return Results
    # ======================================

    return (
        score,
        feedback,
        strengths,
        weaknesses
    )