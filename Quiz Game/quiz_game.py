
import random
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

RESULTS_FILE = BASE_DIR / "quiz_results.txt"
LEADERBOARD_FILE = BASE_DIR / "leaderboard.txt"

quiz_data = {
    "Science": [
        {
            "question": "Which is the largest planet in our solar system?",
            "options": {
                "A": "Earth",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Venus"
            },
            "answer": "C"
        },
        {
            "question": "Which gas do plants absorb during photosynthesis?",
            "options": {
                "A": "Oxygen",
                "B": "Nitrogen",
                "C": "Carbon Dioxide",
                "D": "Hydrogen"
            },
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": {
                "A": "Ag",
                "B": "Au",
                "C": "Fe",
                "D": "Cu"
            },
            "answer": "B"
        },
        {
            "question": "How many bones are there in an adult human body?",
            "options": {
                "A": "206",
                "B": "201",
                "C": "210",
                "D": "215"
            },
            "answer": "A"
        }
    ],

    "Geography": [
        {
            "question": "What is the capital of Japan?",
            "options": {
                "A": "Seoul",
                "B": "Beijing",
                "C": "Bangkok",
                "D": "Tokyo"
            },
            "answer": "D"
        },
        {
            "question": "Which is the largest continent?",
            "options": {
                "A": "Africa",
                "B": "Asia",
                "C": "Europe",
                "D": "Australia"
            },
            "answer": "B"
        },
        {
            "question": "Which is the longest river in the world?",
            "options": {
                "A": "Amazon",
                "B": "Ganga",
                "C": "Nile",
                "D": "Yangtze"
            },
            "answer": "C"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": {
                "A": "China",
                "B": "Japan",
                "C": "Thailand",
                "D": "India"
            },
            "answer": "B"
        }
    ],

    "Technology": [
        {
            "question": "What does CPU stand for?",
            "options": {
                "A": "Central Processing Unit",
                "B": "Computer Personal Unit",
                "C": "Central Program Utility",
                "D": "Computer Processing Utility"
            },
            "answer": "A"
        },
        {
            "question": "Which language is primarily used to structure web pages?",
            "options": {
                "A": "Python",
                "B": "HTML",
                "C": "Java",
                "D": "SQL"
            },
            "answer": "B"
        },
        {
            "question": "Who is known as the father of the computer?",
            "options": {
                "A": "Alan Turing",
                "B": "Charles Babbage",
                "C": "Bill Gates",
                "D": "Steve Jobs"
            },
            "answer": "B"
        },
        {
            "question": "Which of these is an operating system?",
            "options": {
                "A": "Python",
                "B": "Google",
                "C": "Linux",
                "D": "HTML"
            },
            "answer": "C"
        }
    ]
}


def show_categories():
    print("\n========== QUIZ CATEGORIES ==========")
    categories = list(quiz_data.keys())
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")
    return categories

def save_result(name, category, score, total):

    percentage = (score / total) * 100
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(RESULTS_FILE, "a") as file:

        file.write("\n========== QUIZ RESULT ==========\n")
        file.write(f"Name: {name}\n")
        file.write(f"Category: {category}\n")
        file.write(f"Score: {score}/{total}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Date: {current_time}\n")

def update_leaderboard(name, category, score, total):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{category},{score},{total}\n")

def show_leaderboard():
    print("\n========== LEADERBOARD ==========")

    try:
        with open(LEADERBOARD_FILE, "r") as file:
            records = []
            for line in file:
                name, category, score, total = line.strip().split(",")
                records.append(
                    (name, category, int(score), int(total))
                )
            if not records:
                print("No records available.")
                return
            records.sort(
                key=lambda record: record[2] / record[3],
                reverse=True
            )
            for rank, record in enumerate(records, start=1):
                name, category, score, total = record
                percentage = (score / total) * 100
                print(
                    f"{rank}. {name} | {category} | "
                    f"{score}/{total} | {percentage:.2f}%"
                )
    except FileNotFoundError:
        print("No leaderboard records found.")

def play_quiz():
    name = input("\nEnter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    categories = show_categories()
    while True:
        try:
            choice = int(input("\nSelect a category: "))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            else:
                print("Please select a valid category.")
        except ValueError:
            print("Please enter a number.")

    questions = quiz_data[category].copy()

    random.shuffle(questions)
    score = 0
    total = len(questions)
    print(f"\n========== {category.upper()} QUIZ ==========")
    for question_number, question in enumerate(questions, start=1):
        print(f"\nQuestion {question_number}: {question['question']}")
        for option, value in question["options"].items():
            print(f"{option}. {value}")
        while True:
            guess = input(
                "\nEnter your answer (A/B/C/D): "
            ).strip().upper()
            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Enter A, B, C or D.")
        if guess == question["answer"]:
            print("Correct!")
            score += 1
        else:
            correct_answer = question["answer"]
            correct_option = question["options"][correct_answer]
            print(
                f"Incorrect! Correct answer: "
                f"{correct_answer}. {correct_option}"
            )
    percentage = (score / total) * 100

    print("\n========== QUIZ COMPLETED ==========")
    print(f"Player: {name}")
    print(f"Category: {category}")
    print(f"Final Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    save_result(name, category, score, total)

    update_leaderboard(name, category, score, total)

    print("\nYour result has been saved successfully.")

def main():
    while True:
        print("\n========== QUIZ GAME ==========")
        print("1. Play Quiz")
        print("2. View Leaderboard")
        print("3. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                play_quiz()
            elif choice == 2:
                show_leaderboard()
            elif choice == 3:
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Select 1, 2 or 3.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
