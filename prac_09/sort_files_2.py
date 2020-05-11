"""
CP1404/CP5632 Practical
Sort files into categorised folders
"""

import os
import shutil


def main():
    os.chdir('FilesToSort')
    extension_dict = find_extensions()
    move_files(extension_dict)


def find_extensions():
    """Return a dictionary with categories as keys and a list of corresponding extensions as values"""
    extensions = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            if extension not in extensions:
                category = input("What category would you like to sort {} files into? ".format(extension))
                # if category not in [category for categories in extensions.values() for category in categories]:
                extensions[extension] = category

    return extensions


def move_files(extension_dict):
    """Sort the files into their respective category folders"""
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1]
            category = extension_dict[file_extension]
            try:
                os.mkdir(category)
            except FileExistsError:
                print("{} directory already exists".format(category))

            shutil.move(filename, category)


main()
