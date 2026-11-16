# ==========================================
# Coding Interview Evaluator
# ==========================================

import ast


def evaluate_coding_answer(code, question_number):

    code = code.strip()

    # ------------------------------------------
    # Step 1: Check Syntax
    # ------------------------------------------

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return (
            0,
            "Syntax error found. Please check your Python code carefully."
        )

    source = code.lower()

    score = 0
    strengths = []
    weaknesses = []

    # ------------------------------------------
    # Question 1
    # Even or Odd
    # ------------------------------------------

    if question_number == 1:

        # Input check
        if "input(" in source:
            score += 2
            strengths.append("Input handling is present.")
        else:
            weaknesses.append("Use input() to get the number.")

        # If condition check
        has_if = any(
            isinstance(node, ast.If)
            for node in ast.walk(tree)
        )

        if has_if:
            score += 2
            strengths.append("Conditional logic is used.")
        else:
            weaknesses.append("Use an if-else condition.")

        # Modulo operator check
        has_modulo = any(
            isinstance(node, ast.Mod)
            for node in ast.walk(tree)
        )

        if has_modulo:
            score += 3
            strengths.append("Modulo operator is correctly used.")
        else:
            weaknesses.append(
                "Use the modulo (%) operator to check divisibility by 2."
            )

        # Even/Odd output check
        if "even" in source and "odd" in source:
            score += 2
            strengths.append("Both Even and Odd cases are handled.")
        else:
            weaknesses.append(
                "Display appropriate Even and Odd results."
            )

        # Basic code quality
        if "print(" in source:
            score += 1
            strengths.append("Output is displayed using print().")
        else:
            weaknesses.append("Use print() to display the result.")

    # ------------------------------------------
    # Question 2
    # Largest of Two Numbers
    # ------------------------------------------

    elif question_number == 2:

        # Input check
        input_count = source.count("input(")

        if input_count >= 2:
            score += 2
            strengths.append("Two input values are taken.")
        else:
            weaknesses.append(
                "Take two numbers as input."
            )

        # If condition check
        has_if = any(
            isinstance(node, ast.If)
            for node in ast.walk(tree)
        )

        if has_if:
            score += 2
            strengths.append("Conditional logic is used.")
        else:
            weaknesses.append(
                "Use an if-else condition to compare the numbers."
            )

        # Comparison check
        has_comparison = any(
            isinstance(node, ast.Compare)
            for node in ast.walk(tree)
        )

        if has_comparison:
            score += 3
            strengths.append("Comparison between numbers is present.")
        else:
            weaknesses.append(
                "Compare the two numbers using > or <."
            )

        # Print check
        if "print(" in source:
            score += 2
            strengths.append("Largest value is displayed.")
        else:
            weaknesses.append(
                "Use print() to display the largest number."
            )

        # Basic variable usage
        if "=" in code:
            score += 1
            strengths.append("Variables are used to store values.")
        else:
            weaknesses.append(
                "Store the input values in variables."
            )

    # ------------------------------------------
    # Question 3
    # Factorial
    # ------------------------------------------

    elif question_number == 3:

        # Input check
        if "input(" in source:
            score += 2
            strengths.append("Input handling is present.")
        else:
            weaknesses.append(
                "Use input() to get the number."
            )

        # Loop check
        has_loop = any(
            isinstance(node, (ast.For, ast.While))
            for node in ast.walk(tree)
        )

        if has_loop:
            score += 2
            strengths.append("A loop is used to calculate factorial.")
        else:
            weaknesses.append(
                "Use a for loop or while loop."
            )

        # Range check
        if "range(" in source:
            score += 2
            strengths.append("range() is used correctly.")
        else:
            weaknesses.append(
                "Use range() to iterate through the numbers."
            )

        # Multiplication check
        has_multiplication = any(
            isinstance(node, ast.Mult)
            for node in ast.walk(tree)
        )

        if has_multiplication:
            score += 2
            strengths.append("Multiplication logic is present.")
        else:
            weaknesses.append(
                "Multiply the numbers to calculate factorial."
            )

        # Print check
        if "print(" in source:
            score += 1
            strengths.append("Factorial result is displayed.")
        else:
            weaknesses.append(
                "Use print() to display the factorial."
            )

        # Initialization check
        if "= 1" in code or "=1" in code:
            score += 1
            strengths.append(
                "Factorial variable is initialized correctly."
            )
        else:
            weaknesses.append(
                "Initialize the factorial variable with 1."
            )

    # ------------------------------------------
    # Invalid Question Number
    # ------------------------------------------

    else:
        return (
            0,
            "Invalid coding question."
        )

    # ------------------------------------------
    # Generate Feedback
    # ------------------------------------------

    if score >= 9:
        feedback = (
            "Excellent! Your solution correctly implements "
            "the required logic."
        )

    elif score >= 7:
        feedback = (
            "Good solution! Your main logic is correct, "
            "but a few improvements can make it better."
        )

    elif score >= 5:
        feedback = (
            "Fair attempt! Some important parts are correct, "
            "but the solution needs improvement."
        )

    else:
        feedback = (
            "Needs improvement. Check the required logic "
            "and correct the missing parts."
        )

    # Add detailed feedback
    if strengths:
        feedback += "\n\nStrengths:\n"
        for strength in strengths:
            feedback += "✓ " + strength + "\n"

    if weaknesses:
        feedback += "\nAreas to Improve:\n"
        for weakness in weaknesses:
            feedback += "• " + weakness + "\n"

    return score, feedback, strengths, weaknesses