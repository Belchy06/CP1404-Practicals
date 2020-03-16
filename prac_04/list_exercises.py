"""
CP1404/CP5632 Practical
Intermediate Exercises, prac_04
"""


def exercise_1():
    number_of_nums = int(input("Enter the amount of numbers you want: "))
    numbers = get_list_of_numbers(number_of_nums)
    print_number_facts(numbers)


def get_list_of_numbers(number_of_nums):
    numbers = []
    for i in range(1, number_of_nums + 1):
        valid_number = False
        while not valid_number:
            try:
                number = int(input("Number: "))
                valid_number = True
            except:
                print("Please enter a valid number!")
        numbers.append(number)
    return numbers


def print_number_facts(list_of_numbers):
    if len(list_of_numbers) > 0:
        print("The first number is: {}".format(list_of_numbers[0]))
        print("The last number is: {}".format(list_of_numbers[len(list_of_numbers) - 1]))
        print("The smallest number is: {}".format(min(list_of_numbers)))
        print("The largest number is: {}".format(max(list_of_numbers)))
        print("The average of the numbers is: {}".format(sum(list_of_numbers) / len(list_of_numbers)))
    else:
        print("There are no numbers!")


exercise_1()


def exercise_2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = get_username()
    while username not in usernames:
        print("Access denied")
        username = get_username()
    else:
        print("Access granted")


def get_username():
    return input("Enter your username: ")


exercise_2()
