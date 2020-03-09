def print_instructions():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


name = input("Enter name: ")
print_instructions()
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello ", name)
    elif choice == 'G':
        print("Goodbye ", name)
    else:
        print("Invalid option!")
    print_instructions()
    choice = input(">>> ").upper()

print("Finished!")
