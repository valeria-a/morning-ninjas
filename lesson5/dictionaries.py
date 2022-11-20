# friends = 7
# for i in range(friends):
#     print("fsfsd")
#     if i == 3:
#         i += 2

# key-value
my_dict = {
    123456789: "Valeria Aynbinder",
    987765234: "Ziv Attias",
    783465234: "Nehorai Tubul"
}
# print(my_dict[987765234])
# my_dict[333333333] = "Israel Israeli"
# print(my_dict)
#
# d1 = {
#     'Iphone 13': 5,
#     'Samsung Galaxy 22': 10,
#     'MacBook Pro': 8,
#     'a': 17
# }
# print(d1)
#
# d1['a'] = 20
# print(d1)
# d1['b'] = 222
#
# print(d1)

person1 = {
    'first_name': 'Valeria',
    'last_name': 'Aynbinder',
    'year': 1987,
    'id': 333333333,
    'phone': '0546666666'
}
person2 = {
    'first_name': 'Ziv',
    'last_name': 'Attias',
    'year': 1998,
    'id': 111111111,
    'phone': '0546664455'
}

# persons = [person1, person2]
# print(persons)
# for person in persons:
#     print(person['last_name'])

import pprint

persons_dict = {
    person1['id']: person1,
    person2['id']: person2
}
pprint.pprint(persons_dict)

# my_list = [[123456789, "Valeria Aynbinder"],
#            [987765234, "Ziv Attias"],
#            [783465234, "Nehorai Tubul"]]
#
# for elem in my_list:
#     if elem[0] == 783465234:
#         print(elem[1])

empty = {}
empty = dict()

empty_list = []
empty_list = list()

# Implement a function insert_persons that receives int
# number n as argument, and asks the user to insert
# details of n persons. The details for each person include:
# id, first_name, last_name, year, phone.
# The function returns a dictionary with all the
# persons details

# def insert_persons(num: int) -> dict:
#     persons = {}

#     for i in range(num):
#         person = {}
#         person['id'] = input("Id: ")
#         person['first_name'] = input("f_name: ")
#         person['phone'] = input("Phone num: ")
#         #{}
#         #person['id'] = 2343343
#         #persons[2343343] = person
#         persons[person['id']] = person
#     return persons
#
# print(insert_persons(2))


def insert_persons(num: int) -> dict:
    persons = {}
    fields = ('id', 'first_name', 'phone')
    # fields(('id', int), ('first_nanme', str))
    fields = {'id': int,
              'first_name': str}
    for i in range(num):
        person = {}
        for field in fields:
            person[field] = input(f"Insert {field}: ")
        persons[person['id']] = person
    return persons

print(insert_persons(2))
# representing an object

# using operator [] for read and assignment

# iterating over dictionary

# dictionary methods

