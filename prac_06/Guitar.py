"""CP1404 Practical - Programming language do-from-scratch exercise"""

import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """ Initializes a guitar instance with default values """
        self.name = name.title()
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Format the output to be "Name (Year) : Cost" """
        return "{} ({}) : {:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """ Returns the age of the guitar eg.  2020 - 1922 = 98 """
        return datetime.datetime.year() - self.year

    def is_vintage(self):
        """ Returns true or false depending on if the guitar is older than 50 years """
        return self.get_age() > 50
