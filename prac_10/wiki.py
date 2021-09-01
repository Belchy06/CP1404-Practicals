"""
CP1404/CP5632 Practical
Testing wikipedia framework
"""

import wikipedia


def main():
    query = input("Enter a page title / search phrase: ")
    try:
        query_page = wikipedia.page(query)
        print("Title: {}".format(query_page.title))
        print("Summary: {}".format(wikipedia.summary(query)))
        print("Url: {}".format(query_page.url))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

main()