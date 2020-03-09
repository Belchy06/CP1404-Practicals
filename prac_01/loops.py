# Example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(10, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
numStars = int(input("Enter the number of stars: "))
for i in range(0, numStars, 1):
    print("*", end='')
print()

# d.
for i in range(1, numStars + 1, 1):
    for j in range(0, i):
        print("*", end='')
    print()
