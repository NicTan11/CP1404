"""
1. Password stars
Convert passwords from words to stars.
"""
MINIMUM_LENGTH = 4
PASSWORD_PROMPT = f"Enter password of at least {MINIMUM_LENGTH} characters: "


def get_password(minimum_length):
    while True:
        try:
            password = input(PASSWORD_PROMPT)
            if len(password) < minimum_length:
                raise ValueError(f"Password must be at least {minimum_length} characters long")
            return password
        except ValueError as e:
            print(e)


def print_asterisks(sequence):
    print('*' * len(sequence))


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


main()
