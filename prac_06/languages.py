"""
CP1404 Practical - Programming language intermediate exercise
"""

from prac_06.ProgrammingLanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    programming_languages = [ruby, python, visual_basic]

    dynamic_languages = [language.name for language in programming_languages if language.is_dynamic()]
    print("The dynamically typed languages are:")
    print(*dynamic_languages, sep='\n')


main()
