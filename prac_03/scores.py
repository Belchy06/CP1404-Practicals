"""
CP1404 Practical 3

Ask user for a number of scores and print the result for that many generate scores. Created by William Belcher, March 2020.
"""
import random


def get_number_of_scores():
    """
    Get the number of scores the user wants to use
    """
    valid_number = False
    number_of_scores = 0
    while not valid_number:
        try:
            number_of_scores = int(input("Please enter the number of scores you want: "))
            valid_number = True
        except:
            print("Please enter a valid number!")
    return number_of_scores


def generate_scores(number_of_scores):
    """
    Generate a list of scores the same length as the number of scores required
    """
    scores = []
    for i in range(number_of_scores):
        scores.append(random.randint(0, 100))
    return scores


def calculate_result(score):
    """
    Calculate the score based on the result
    """
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


def main():
    number_of_scores = get_number_of_scores()
    list_of_scores = generate_scores(number_of_scores)
    for score in list_of_scores:
        result = calculate_result(score)
        print("{} is {}".format(score, result))


main()
