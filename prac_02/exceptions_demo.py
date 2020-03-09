try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    """
    Added lines below
    """
    while denominator <= 0:
        denominator = int(input("Please enter a value larger than 0 for the denominator: "))
    """
    end of added lines
    """
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1. ValueError occurs whenever the number entered is not a number
2.
3.
"""
