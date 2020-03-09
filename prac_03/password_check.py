MIN_LENGTH = 5


def validate_password(user_input):
    return len(user_input) >= MIN_LENGTH


def main():
    password = get_password()

    print_password(password)


def print_password(password):
    for char in password:
        print("*", end="")


def get_password():
    password = input("Please enter a password greater than or equal to {} characters: ".format(MIN_LENGTH))
    while not validate_password(password):
        password = input("Please enter a password greater than or equal to {} characters: ".format(MIN_LENGTH))
    return password


main()
