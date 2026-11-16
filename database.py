import sqlite3


# ==========================================
# Database Connection
# ==========================================

def get_connection():

    connection = sqlite3.connect(
        "interview.db"
    )

    return connection


# ==========================================
# Create Interview Results Table
# ==========================================

def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interview_results (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            interview_type TEXT,

            total_score INTEGER,

            maximum_score INTEGER,

            percentage REAL,

            performance TEXT,

            interview_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


# ==========================================
# Save Interview Result
# ==========================================

def save_result(
    interview_type,
    total_score,
    maximum_score,
    percentage,
    performance
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO interview_results
        (
            interview_type,
            total_score,
            maximum_score,
            percentage,
            performance
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        interview_type,
        total_score,
        maximum_score,
        percentage,
        performance
    ))

    connection.commit()

    connection.close()
# ==========================================
# Get Interview History
# ==========================================

def get_results():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM interview_results
        ORDER BY id DESC
    """)

    results = cursor.fetchall()

    connection.close()

    return results
# ==========================================
# Get Dashboard Statistics
# ==========================================

def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor()

    # Total number of interviews
    cursor.execute("""
        SELECT COUNT(*)
        FROM interview_results
    """)

    total_interviews = cursor.fetchone()[0]


    # Average percentage
    cursor.execute("""
        SELECT AVG(percentage)
        FROM interview_results
    """)

    average_score = cursor.fetchone()[0]


    # Best percentage
    cursor.execute("""
        SELECT MAX(percentage)
        FROM interview_results
    """)

    best_score = cursor.fetchone()[0]


    connection.close()


    # If there are no interviews
    if average_score is None:
        average_score = 0

    if best_score is None:
        best_score = 0


    return (
        total_interviews,
        average_score,
        best_score
    )
# ==========================================
# Get Performance Data
# ==========================================

def get_performance_data():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            interview_type,
            percentage,
            performance,
            interview_date
        FROM interview_results
        ORDER BY id ASC
    """)

    results = cursor.fetchall()

    connection.close()

    return results