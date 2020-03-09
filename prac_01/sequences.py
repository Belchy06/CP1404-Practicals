# Print even numbers function
def print_even(m, n):
    print("Even numbers")
    # Really weird ternary to see if min value is odd and if so add one. if max value is even then add 1 so the max
    # value appears in output
    for i in range(m if m % 2 == 0 else m + 1, n if n % 2 != 0 else n + 1, 2):
        print(i, end=' ')
    print()


def print_odd(m, n):
    print("Odd numbers")
    # Really weird ternary to see if min value is even and if so add one. if max value is odd then add 1 so the max
    # value appears in output
    for i in range(m if m % 2 != 0 else m + 1, n if n % 2 == 0 else n + 1, 2):
        print(i, end=' ')
    print()


def print_square(m, n):
    print("Square numbers")
    i = 1
    while True:
        square = i * i
        # if the square is less than the minimum, increment the number we square
        if square < m:
            i += 1
        # else if the square falls within the range, print it and add one to the number we square
        elif m <= square <= n:
            print(square, end=' ')
            i += 1
        # else break the loop
        else:
            break
    print()


def print_instructions():
    print("What would you like to do?")
    print("(E)ven numbers")
    print("(O)dd numbers")
    print("(S)quare numbers")
    print("(Q)uit")


print("Welcome to the number game!")
x = int(input("Enter your value for x: "))
y = int(input("Enter your value for y: "))
print_instructions()
choice = input()
while choice != 'Q' or choice != 'q':
    if choice == 'E' or choice == 'e':
        print_even(x, y)
    elif choice == 'O' or choice == 'o':
        print_odd(x, y)
    elif choice == 'S' or choice == 's':
        print_square(x, y)
    else:
        print("Invalid selection!")
    print_instructions()
    choice = input()
# End
print("Thanks for playing!")
