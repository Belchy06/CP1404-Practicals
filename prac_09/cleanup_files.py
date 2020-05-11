"""
CP1404/CP5632 Practical
Cleanup file names
"""

import shutil
import os

def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        #print(split_camel_case(filename))

        print(get_fixed_filename(filename))
        #rint("Renaming {} to {}".format(filename, new_name))

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    temp = []
    for index, char in enumerate(new_name):
        # If the character is uppercase and not the first in the word
        if char.isupper() and index != 0:
            # If the preceding character is an not an underscore, add the underscore in
            if new_name[index - 1] != "_":
                temp.append("_")
                temp.append(char)
            # The underscore is already there so just append the character normally
            else:
                temp.append(char)

        # Else if the current char is lowercase and there is a preceding opening bracket
        elif new_name[index - 1] == "(" and char.islower():
            # Capitalize the current char
            temp.append(char.upper())

        # Else just append the normal character
        else:
            temp.append(char)

    return "".join(temp)


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


#main()
demo_walk()