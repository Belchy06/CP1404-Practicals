"""
CP1404/CP5632 Practical
Stores the email and name of a user in a dictionary
"""
email_dictionary = {}
email = input("Email: ")
email_name = email.split('@')
name = email_name[0].split('.')
name2 = " ".join(name)
name3 = name2.title()
prompt = input("Is your name {}? (y/n): ".format(name3)).lower()
if prompt[0] == 'y':
    print('yes')
    email_dictionary[email] = name3
elif prompt[0] == 'n':
    print('n')
    user_name = input("Name: ")
    email_dictionary[email] = user_name
else:
    print("other")

print(email_dictionary)

for email, name in email_dictionary.items():
    print("{} ({})".format(name, email))
