"""
CP1404/CP5632 Practical
Stores the email and name of a user in a dictionary
"""

email = input("Email: ")
email_name = email.split('@')
name = email_name[0].split('.')
name2 = " ".join(name)
name3 = name2.title()
prompt = input("Is your name {}? (y/n): ".format(name3)).lower()
if prompt[0] == 'y':
    print('yes')
elif prompt[0] == 'n':
    print('n')
else:
    print("other")
