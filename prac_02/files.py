NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

name = input("Please enter your name: ")
out_file = open(NAME_FILE, 'w')
print(name, file=out_file)
out_file.close()

open_file = open(NAME_FILE, 'r')
print("Your name is:", open_file.read())
open_file.close()


number_file = open(NUMBER_FILE, 'r')
print(int(number_file.readline()) + int(number_file.readline()))
number_file.close()

number_file = open(NUMBER_FILE, 'r')
print(sum(map(int, number_file.readlines())))
number_file.close()
