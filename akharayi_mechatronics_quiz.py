"""
Mechatronics Quiz App
Author: Akharayi Joshua Osamudiamwen

A beginner-friendly multiple-choice quiz with automatic scoring.
Extra feature: the app reviews the questions answered incorrectly.
"""

import random


STUDENT_NAME = "Akharayi Joshua Osamudiamwen"

# Each question stores: question, options, correct option number, explanation.
questions = [
    (
        "Which device converts electrical energy into mechanical motion?",
        ["A. Sensor", "B. Actuator", "C. Resistor", "D. Fuse"],
        2,
        "An actuator converts an input signal or energy into physical action."
    ),
    (
        "Which sensor is commonly used to detect nearby metallic objects?",
        ["A. Inductive proximity sensor", "B. Thermocouple",
         "C. Microphone", "D. Photoresistor"],
        1,
        "An inductive proximity sensor detects metallic objects without contact."
    ),
    (
        "What is the main purpose of a microcontroller in a mechatronic system?",
        ["A. To provide structural support", "B. To store fuel",
         "C. To process inputs and control outputs", "D. To reduce friction"],
        3,
        "A microcontroller reads inputs, processes instructions and controls outputs."
    ),
    (
        "Which component is commonly used to measure temperature?",
        ["A. Relay", "B. Thermistor", "C. Gear", "D. Bearing"],
        2,
        "A thermistor changes resistance as temperature changes."
    ),
    (
        "What does PLC stand for in industrial automation?",
        ["A. Power Level Circuit", "B. Program Line Connection",
         "C. Process Logic Current", "D. Programmable Logic Controller"],
        4,
        "PLC means Programmable Logic Controller."
    ),
    (
        "Which type of motor moves in controlled angular steps?",
        ["A. Stepper motor", "B. Induction heater", "C. Transformer", "D. Alternator"],
        1,
        "A stepper motor moves through discrete steps for controlled positioning."
    ),
    (
        "What is the function of a gear train?",
        ["A. To measure temperature", "B. To transmit motion and torque",
         "C. To store program instructions", "D. To detect light"],
        2,
        "A gear train transmits rotary motion and can change speed or torque."
    ),
    (
        "Which control system uses feedback to compare actual output with a setpoint?",
        ["A. Open-loop system", "B. Manual-only system",
         "C. Closed-loop system", "D. Mechanical lock"],
        3,
        "A closed-loop control system uses feedback to correct output error."
    ),
    (
        "Which device converts a physical quantity into a signal that a controller can read?",
        ["A. Sensor", "B. Coupling", "C. Pulley", "D. Chassis"],
        1,
        "A sensor detects a physical quantity and produces a corresponding signal."
    ),
    (
        "What is the SI unit of electrical power?",
        ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
        4,
        "Electrical power is measured in watts (W)."
    ),
]


def get_menu_choice():
    """Get a valid menu selection and return it as an integer."""
    while True:
        try:
            choice = int(input("Choose an option (1-4): "))
            if 1 <= choice <= 4:
                return choice
            print("Please enter a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def ask_question(question_data, number, total):
    """Display one question and return whether the answer is correct."""
    question_text, options, correct_answer, explanation = question_data

    print(f"\\nQuestion {number} of {total}")
    print(question_text)
    for option in options:
        print(option)

    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            print("Please choose a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Enter 1, 2, 3 or 4.")

    if answer == correct_answer:
        print("Correct!")
        return True

    print(f"Not quite. The correct option is {correct_answer}.")
    print(f"Explanation: {explanation}")
    return False


def calculate_percentage(score, total):
    """Calculate and return the quiz score as a percentage."""
    if total == 0:
        return 0.0
    return (score / total) * 100


def get_result_message(percentage):
    """Return a performance message based on the percentage."""
    if percentage >= 80:
        return "Excellent work! You have a strong understanding."
    elif percentage >= 60:
        return "Good effort! Keep revising and practising."
    elif percentage >= 40:
        return "Fair attempt. Review the topics and try again."
    else:
        return "Keep learning. Go through the explanations and practise again."


def run_quiz():
    """Run one quiz attempt, show the result and review missed questions."""
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)  # Extra feature: random question order.

    score = 0
    missed_questions = []

    print("\\n" + "=" * 55)
    print("WELCOME TO THE MECHATRONICS QUIZ APP")
    print(f"Student: {STUDENT_NAME}")
    print("=" * 55)
    print("Answer each question by entering its option number.")

    for index, question_data in enumerate(shuffled_questions, start=1):
        was_correct = ask_question(question_data, index, len(shuffled_questions))
        if was_correct:
            score += 1
        else:
            missed_questions.append(question_data)

    percentage = calculate_percentage(score, len(shuffled_questions))

    print("\\n" + "=" * 55)
    print("QUIZ RESULTS")
    print(f"Student: {STUDENT_NAME}")
    print(f"Score: {score} out of {len(shuffled_questions)}")
    print(f"Percentage: {percentage:.1f}%")
    print(get_result_message(percentage))
    print("=" * 55)

    # Extra feature: review every question answered incorrectly.
    if missed_questions:
        print("\\nREVISION: QUESTIONS TO REVIEW")
        for index, item in enumerate(missed_questions, start=1):
            question_text, options, correct_answer, explanation = item
            print(f"\\n{index}. {question_text}")
            print(f"Correct answer: {options[correct_answer - 1]}")
            print(f"Explanation: {explanation}")
    else:
        print("\\nGreat job! You answered every question correctly.")


def main():
    """Start the app and allow the student to take the quiz again."""
    while True:
        run_quiz()
        print("\\n1. Take the quiz again")
        print("2. Exit")
        choice = get_menu_choice()

        if choice == 2:
            print(f"Thank you for using the Mechatronics Quiz App, {STUDENT_NAME}!")
            break


if __name__ == "__main__":
    main()
