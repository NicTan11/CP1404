"""
#5. Exceptions_to_complete
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set flag to True to exit the loop if an integer is entered
    except ValueError:  # Catch the ValueError exception when input is not a valid integer
        print("Please enter a valid integer.")
print("Valid result is:", result)
