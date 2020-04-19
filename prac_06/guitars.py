"""
CP1404 Practical - Programming language do-from-scratch exercise
"""

from prac_06.Guitar import Guitar


def main():
    guitars = []

    # Test code
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = get_year_input()
        cost = get_cost_input()
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print("{guitar.name} ({guitar.year}) : {guitar.cost} added".format(guitar=guitar_to_add))

    print_guitars(guitars)


def get_cost_input():
    """
    Validate the cost input required to be above 0
    """
    valid_input = False
    while not valid_input:
        try:
            user_input = float(input("Cost: $"))
            if user_input < 0:
                print("Cost must be greater than or equal to 0")
            else:
                valid_input = True
        except:
            print("Cost must be greater than or equal to 0")
            user_input = float(input("Cost: $"))
    return user_input


def get_year_input():
    """
    Validate the year input required to be above 0
    """
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input("Year: "))
            if user_input < 0:
                print("Year must be greater than or equal to 0")
            else:
                valid_input = True
        except:
            print("Year must be greater than or equal to 0")
            user_input = int(input("Year: "))
    return user_input


def print_guitars(guitar_list):
    """
    Enumerate over the guitar_list and print the required information with the correct formatting
    """
    for index, guitar in enumerate(guitar_list, 1):
        print("Guitar {}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {}"
              .format(index,
                      "(vintage)" if guitar.is_vintage() else "",
                      guitar=guitar))


main()
