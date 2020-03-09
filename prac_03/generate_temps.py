import random

FILE_NAME = "temps_input.txt"
NUMBER_OF_TEMPS = 15
MAX_TEMP = 200.00
MIN_TEMP = -200.00


def main():
    out_file = open(FILE_NAME, 'w')
    for i in range(NUMBER_OF_TEMPS):
        print(random.uniform(MIN_TEMP, MAX_TEMP), file=out_file)
    out_file.close()


main()
