"""
CP1404/CP5632 Practical
Sort files into respective folders
"""

import os
import shutil


def main():
    os.chdir('FilesToSort')
    extensions = find_extensions()
    for extension in extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            print("{} directory already exists".format(extension))
    move_files()


def find_extensions():
    """Return a list of all the extension types present"""
    extensions = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            if extension not in extensions:
                extensions.append(extension)
    return extensions


def move_files():
    """Sort the files into their respective folders"""
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            shutil.move(filename, extension)


main()
