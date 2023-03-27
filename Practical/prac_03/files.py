"""
6. files
"""
# 1. Writing name to file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# 2. Reading name from file and printing
with open("name.txt", 'r') as file:
    name = file.read().strip()
    print(f"Your name is {name}")

# 3. Adding first two numbers from file
with open("numbers.txt", 'r') as file:
    line1 = int(file.readline().strip())
    line2 = int(file.readline().strip())
    total = line1 + line2
    print(f"Total: {total}")

# 4. Adding all numbers in file
with open("numbers.txt", 'r') as file:
    total = 0
    for line in file:
        number = int(line.strip())
        total += number
    print(f"Total: {total}")
