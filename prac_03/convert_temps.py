"""
CP1404 Practical 3

Read a file containing Fahrenheit values and convert them to Celsius values that's then saved to a new file. Created by William Belcher, March 2020.
"""
INPUT_FILE = "temps_input.txt"
OUTPUT_FILE = "temps_output.txt"


def read_input_file():
    """
    Read each line of input file and save value to array
    """
    list_of_temps = []
    input_file = open(INPUT_FILE, 'r')
    with input_file:
        for line in input_file:
            list_of_temps.append(float(line.strip()))
    input_file.close()
    return list_of_temps


def write_output_file(output_temps):
    """
    Write each value in input array to a line in the output file
    """
    output_file = open(OUTPUT_FILE, 'w')
    for temp in output_temps:
        print(temp, file=output_file)
    output_file.close()


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert fahrenheit to celsius
    """
    return 5 / 9 * (fahrenheit - 32)


def main():
    list_of_fahrenheit = read_input_file()
    list_of_celsius = []
    for fahrenheit in list_of_fahrenheit:
        list_of_celsius.append(fahrenheit_to_celsius(fahrenheit))
    write_output_file(list_of_celsius)


main()
