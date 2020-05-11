"""
CP1404/CP5632 Practical
SilverServiceTaxi test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    print("{}, Fare: ${}".format(taxi, taxi.get_fare()))


main()
