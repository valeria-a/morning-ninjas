# student = {
#     'name': 'David',
#     'city': 'Tel Aviv',
#     'grades': {'math':[98, 87, 90],
#                'english': [85]
#                }
# }
#
# import json
#
# dict_as_str = json.dumps(student)
# print(type(dict_as_str))
# print(dict_as_str)
#
# with open('student.json', 'w') as fh:
#     json.dump(student, fh)
#
# with open('student.json', 'r') as fh:
#     reloaded_student = json.load(fh)
#
# reloaded_student[0]['grades']['math'][2]