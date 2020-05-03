"""
CP1404/CP5632 Practical
Taxi Simulator
"""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU_STRING = "q)uit, c)hoose, d)rive"

def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.00
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            if current_taxi != None:
                taxis[current_taxi].start_fare()
                distance = get_distance_to_drive()
                taxis[current_taxi].drive(distance)
                trip_cost = taxis[current_taxi].get_fare()
                bill_to_date += trip_cost
                print("Your {} trip cost you ${:.2f}".format(taxis[current_taxi].name, trip_cost))
                print("Bill to date: ${:.2f}".format(bill_to_date))
            else:
                print("You need to choose a taxi first!")
        elif choice == "C":
            current_taxi = get_chosen_taxi(taxis)
            print("Bill to date: ${:.2f}".format(bill_to_date))
        else:
            print("Invalid option!")

        print(MENU_STRING)
        choice = input(">>> ").upper()

    print("Total trip cost: ${:,2f}".format(bill_to_date))
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


def get_chosen_taxi(taxis):
    """

    """
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))

    valid_choice = False
    while not valid_choice:
        try:
            chosen_taxi = int(input("Choose taxi: "))
            # Check if the chosen index is larger than the amount of elements in the song_list
            if chosen_taxi >= len(taxis):
                print("Invalid choice")
            # Check if the number entered is less than 0
            elif chosen_taxi < 0:
                print("Enter a number larger than or equal to 0!")
            # If the chosen index meets these two criteria then it is valid and can be returned by the function
            else:
                valid_choice = True
        # User entered characters instead of a number
        except ValueError:
            print("Please enter a valid number!")
    return chosen_taxi


def get_distance_to_drive():
    """

    """
    distance = 0
    try:
        distance = int(input("Drive how far? "))
    except ValueError:
        print("Please enter a valid number")
    return distance


main()
