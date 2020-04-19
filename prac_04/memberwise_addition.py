"""
CP1404
Memberwise addition
"""


def add_memberwise(list1, list2):
    added_list = [a + b for a,b in zip(list1, list2)]
    return added_list


def main():
    list1 = [1,2,3]
    list2 = [1,2,3,4]
    added_list = add_memberwise(list1, list2)
    print(added_list)


main()
