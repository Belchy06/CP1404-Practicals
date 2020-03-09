finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a number: "))
        finished = True
    except:
        print("Please enter a valid integer!")
print("The valid result is: ", result)
