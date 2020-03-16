"""
CP1404/CP5632 Practical
Quick Pick Generator
"""
import random

POSSIBLE_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 45]
NUMBERS_PER_LINE = 6


def generate_quick_picks(number_of_picks):
    # Initialize a two dimensional array with dimensions of number_of_picks rows and NUMBERS_PER_LINE columns
    quick_picks = [[0 for j in range(NUMBERS_PER_LINE)] for i in range(number_of_picks)]
    for i in range(number_of_picks):
        for j in range(NUMBERS_PER_LINE):
            rand_num = random.choice(POSSIBLE_NUMBERS)
            # Check if the random number is already in this row
            while rand_num in quick_picks[i]:
                rand_num = random.choice(POSSIBLE_NUMBERS)
            # If the random number is not present in the row, assign it to this position
            quick_picks[i][j] = rand_num
    return quick_picks


def get_number_of_picks():
    valid_number = False
    while not valid_number:
        try:
            number_of_picks = int(input("How many quick picks? "))
            if number_of_picks > 0:
                valid_number = True
            else:
                print("Enter a number larger than 0!")
        except:
            print("Please enter a valid number!")
    return number_of_picks


def print_quick_picks(quick_picks):
    for row in range(len(quick_picks)):
        for column in range(len(quick_picks[0])):
            print(quick_picks[row][column], end=" ")
        print("")


def main():
    number_of_picks = get_number_of_picks()
    quick_picks = generate_quick_picks(number_of_picks)
    print_quick_picks(quick_picks)


main()
