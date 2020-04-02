"""
CP1404/CP5632 Practical
Stores the email and name of a user in a dictionary
"""


def main():
    email_dictionary = {}

    user_email = get_user_email()
    while user_email != "":
        user_name = extract_user_from_email(user_email)
        confirmed_user_name = confirm_username(user_name)
        email_dictionary[user_email] = confirmed_user_name
        user_email = get_user_email()

    print_email_dictionary(email_dictionary)


def get_user_email():
    email = input("Email: ")
    return email


def extract_user_from_email(input_email):
    split_email = input_email.split('@')
    name_array = split_email[0].split('.')
    user_name = " ".join(name_array).title()
    return user_name


def confirm_username(original_name):
    username = original_name
    response = input("Is your name {}? (y/n): ".format(original_name)).lower()
    valid_response = False
    while not valid_response:
        if response == "":
            valid_response = True
        elif response[0] == 'y':
            valid_response = True
        elif response[0] == 'n':
            specified_name = input("Name: ")
            while specified_name == "":
                specified_name = input("Name: ")
            username = specified_name
            valid_response = True
        else:
            response = input("Is your name {}? (y/n): ".format(original_name)).lower()
    return username


def print_email_dictionary(dictionary):
    print()
    for email, name in dictionary.items():
        print("{} ({})".format(name, email))


main()
