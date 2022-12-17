sorted([3, 1, -5, 6, 9])
sorted([3, 1, -5, 6, 9], reverse=True)
students = [
    {"name": "Moshe", "grade": 89},
    {"name": "David", "grade": 93},
    {"name": "Jack", "grade": 73},
]

def my_key_func(student):
    return student["grade"]

sorted(students, key=my_key_func)

sorted(students, key=my_key_func, reverse=True)

# List elements: (Student's Name, Grade, Age)
# sort first by highest grade, then smallest age

participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

# comparing tuples
# (3, 2) > (3, 4)

def multi_key_func(participant):
    return 100 - participant[1], participant[2]

sorted(participant_list, key=multi_key_func)