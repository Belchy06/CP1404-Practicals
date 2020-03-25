"""
CP1404/CP5632 Practical
Hexadecimal colours in a dictionary
"""

HEX_TO_NAME = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc",
    "antiquewhite3": "#cdc0b0",
    "antiquewhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6",
    "aquamarine4": "#458b74",
    "azure1": "#f0ffff"
}

# Take the acronym the user enters and find the associated state name
hex_name = input("Enter colour: ").lower()
while hex_name != "":
    if hex_name in HEX_TO_NAME:
        print(hex_name, "is", HEX_TO_NAME[hex_name])
    else:
        print("Invalid colour name!")
    hex_name = input("Enter colour: ").lower()
