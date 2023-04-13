"""
CP1404/CP5632 Practical Suggested Solution
Data file -> lists program
"""


FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    """Read data from file formatted like: code,lecturer,number of students."""
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            try:
                parts[2] = int(parts[2])
            except ValueError:
                print(f"Invalid data: {line}")
            else:
                subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display data nicely."""
    for subject_data in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()
