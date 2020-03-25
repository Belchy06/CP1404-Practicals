"""
CP1404/CP5632 Practical
Prints the number of occurrences of each string in a user entered string
"""

word_occurrences = {}

input_string = input("Enter your string: ").lower().split()
if input_string != "":
    for string in input_string:
        try:
            word_occurrences[string] += 1
        except KeyError:
            word_occurrences[string] = 1

print(word_occurrences)