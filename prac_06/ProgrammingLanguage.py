"""CP1404 Practical - Programming language intermediate exercise"""


class ProgrammingLanguage:
    def __init__(self, typing="", reflection=False, year=""):
        """
        Initialize the class with the default values

        reflection = boolean
        """

        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return ""

    def is_dynamic(self):
        return self.typing == "Dynamic"
