import random

NUM_QUICK_PICKS = 5
NUM_NUMBERS_PER_QUICK_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

for i in range(NUM_QUICK_PICKS):
    numbers = set()
    while len(numbers) < NUM_NUMBERS_PER_QUICK_PICK:
        numbers.add(random.randint(MIN_NUMBER, MAX_NUMBER))

    print(" ".join("{:2d}".format(num) for num in sorted(numbers)))
