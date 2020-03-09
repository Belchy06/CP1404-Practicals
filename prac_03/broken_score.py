"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def calculate_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


def main():
    score = float(input("Enter score: "))
    print(calculate_result(score))


main()

test_score = 25
print(calculate_result(test_score))
