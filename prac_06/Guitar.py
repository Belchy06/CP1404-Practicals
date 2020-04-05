"""CP1404 Practical - Programming language do-from-scratch exercise"""

import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return datetime.datetime.year() - self.year

    def is_vintage(self):
        return self.get_age() > 50
