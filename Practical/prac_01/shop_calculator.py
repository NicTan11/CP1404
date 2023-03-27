"""
# 4. Shop Calculator
Quickly calculate the total price for a number of items, each with different prices.
if total is more than $100, then a 10% discount is applied.
"""
while True:
    num_items = int(input("Number of items: "))
    try:
        num_items = int(num_items)
        if num_items < 0:
            print("Invalid number of items!")
        else:
            break
    except ValueError:
        print("Invalid number of items!")

total_price = 0
for i in range(num_items):
    while True:
        try:
            price = float(input("Price of item: "))
            break
        except ValueError:
            print("Invalid price!")
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_items} items is ${total_price:.2f}")
