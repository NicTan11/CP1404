"""
1. string formatting
"""
# 1. Using f-strings
year = 1922
make = "Gibson"
model = "L-5 CES"
cost = 16035.4
print(f"{year} {make} {model} for about ${cost:,.2f}!")

# 2. Using a for loop with string formatting
for i in range(0, 151, 50):
    print(f"{i:>3}")
