numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])  #3
print(numbers[-1]) #2
print(numbers[3]) #1
print(numbers[:-1]) #3, 1, 4, 1, 5, 9
print(numbers[3:4]) #1
print(5 in numbers) #True
print(7 in numbers) #False
print("3" in numbers) #False
numbers + [6, 5, 3]
print(numbers) #3, 1, 4, 1, 5, 9, 2, 6, 5, 3

# Section 2
numbers[0] = "ten"

numbers[6] = 1

print(numbers[2:])

print(9 in numbers)
