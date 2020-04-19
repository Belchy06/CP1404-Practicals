"""
CP1404 Practical - Programming language do-from-scratch exercise
"""

from prac_06.Guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 10000)
    vintage = Guitar("Vintage", 1970, 10000)

    print("{} get_age() - Expected 98. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another.name, another.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(vintage.name, vintage.is_vintage()))


main()