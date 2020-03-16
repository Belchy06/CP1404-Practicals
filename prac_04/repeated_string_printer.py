"""
CP1404 prac_04
A program that prints the repeated strings from a sequence of string entered by the user
"""


def print_instructions():
    print("Enter a string after each prompt")
    print("Enter a blank input to see the repeated strings you entered")


def get_string_sequence():
    sequence = []
    string = input("Enter a string!: ")
    while string is not "":
        sequence.append(string)
        string = input("Enter a string!: ")
    return sequence


def find_repeated_strings(string_sequence):
    repeated_strings = []
    repeated_string = [string for string in string_sequence if string_sequence.count(string) >= 2]
    for index, string in enumerate(repeated_string):
        if repeated_string[index] not in repeated_strings:
            repeated_strings.append(repeated_string[index])
    return repeated_strings


def print_repeated_strings(repeated_strings):
    if len(repeated_strings) > 0:
        print("Strings repeated: ", end="")
        for index, string in enumerate(repeated_strings):
            print(string, end=", ")
    else:
        print("There were no repeated strings")


def main():
    print_instructions()
    string_sequence = get_string_sequence()
    repeated_strings = find_repeated_strings(string_sequence)
    print_repeated_strings(repeated_strings)


main()
