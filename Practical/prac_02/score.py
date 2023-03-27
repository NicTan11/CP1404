"""
3. Score
Program to tell the user if their score is invalid, bad, passable or excellent
If score are between 0 and 100 inclusive, 90 or more is excellent, 50 or more is pass,
below 50 is bad.
"""
import random


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_score_result(user_score)
    print(user_result)

    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random score: {random_score}, result: {random_result}")


def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
