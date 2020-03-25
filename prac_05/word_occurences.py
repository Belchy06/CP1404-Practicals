"""
CP1404/CP5632 Practical
Prints the number of occurrences of each string in a user entered string
"""


def main():
    user_input = get_input_string()
    word_occurrences = find_occurrences(user_input)
    print_occurrences(word_occurrences)


def get_input_string():
    input_string = input("Enter your string: ").lower().split()
    while input_string == "":
        input_string = input("Enter your string: ").lower().split()
    return input_string


def find_occurrences(input_string):
    word_occurrences = {}
    for string in input_string:
        try:
            word_occurrences[string] += 1
        except KeyError:
            word_occurrences[string] = 1
    return word_occurrences


def print_occurrences(word_occurrences):
    string_spacing = len(max(word_occurrences, key=len))
    for key, value in word_occurrences.items():
        print("{:{}}: {}".format(key, string_spacing, value))


main()
