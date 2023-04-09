numbers = [3, 1, 4, 1, 5, 9, 2]
# Answers to questions
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modify list elements
numbers[0] = "ten"
numbers[-1] = 1

# Print elements using slicing
print(numbers[2:])

# Check if 9 is an element of numbers
print(9 in numbers)

# Output [4, 1, 5, 9, 1] = True
