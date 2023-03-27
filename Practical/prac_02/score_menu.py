"""
4. score_menu
Programs has a menu which ask the user for their score and show them alot more options.
"""


def main():
    score = None

    while True:
        print("Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").lower()

        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            print_result(score)
        elif choice == "s":
            show_stars(score)
        elif choice == "q":
            print("Goodbye!, Goodluck!!")
            break
        else:
            print("Invalid choice. Please try again.")


def get_valid_score():
    while True:
        score = input("Enter score (0-100): ")
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                return score
        print("Invalid score. Please try again.")


def print_result(score):
    if score is None:
        print("No score has been entered yet.")
    else:
        result = determine_score_result(score)
        print(f"Score: {score}, Result: {result}")


def show_stars(score):
    if score is None:
        print("No score has been entered yet.")
    else:
        stars = "*" * score
        print(stars)


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
