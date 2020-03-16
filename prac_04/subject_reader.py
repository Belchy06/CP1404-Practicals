"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # parts[0] = subject, parts[1] = name, parts[2] = num of students

        print("{0} is taught by {1:5} and has {2:1} students".format(parts[0], parts[1], parts[2]))  # See if that worked
        print("----------")
    input_file.close()


main()