"""
Shop
The total is usually a few cents off due to floating point error. Could be fixed by using a decimal type
"""

numItems = int(input("Number of items: "))
while numItems <= 0:
    print("Invalid number of items entered!")
    numItems = int(input("Number of items: "))

prices = []

for i in range(numItems):
    price = float(input("Price of item: $"))
    prices.append(price)

total = sum(prices)

if total > 100:
    total *= 0.9

print("The total for {} items is ${:.2f}".format(numItems, round(total, 2)))
