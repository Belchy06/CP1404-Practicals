"""
CP1404/CP5632 Practical
Taxi test
"""

from prac_08.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print("{}, Fare: ${}".format(taxi, taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print("{}, Fare: ${}".format(taxi, taxi.get_fare()))


main()
