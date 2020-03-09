finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a number: "))
    except:
        print("Please enter a valid integer!")
print("The valid result is: ", result)
