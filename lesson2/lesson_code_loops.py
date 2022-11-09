# # insert 3 grades and print avg
# count = 0
# grades = []
# grades_sum = 0
# while count < 3:
#     grade = int(input("Insert grade: "))
#     grades.append(grade)
#     grades_sum = grades_sum + grade
#     count = count + 1
# print(f"All the grades: {grades}")
# print(f"The avg is: {grades_sum / len(grades)}")


# drink_type = input("Insert drink: ").lower().strip()  #beer / wine
# while drink_type not in ["beer", "wine"]:
#     drink_type = input("Incorrect input. Insert drink: ").lower().strip()
# print(f"You inserted {drink_type}")


# while True:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         break
# print(f"You inserted {drink_type}")

# incorrect_input = True
# while incorrect_input:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         incorrect_input = False
# print(f"You inserted {drink_type}")

# while False:
#     pass

# ---------------------------------
end_of_input = False
temp_max = None
while not end_of_input:
    i = input("Insert num or $ to finish: ")
    if i == '$':
        end_of_input = True
    else:
        num = int(i)
        if temp_max is None:
            temp_max = num
        if num > temp_max:
            temp_max = num
print("MAx num", temp_max)


# ---------------------------------

# get input 3 digits from user
number_list = list(input("Please insert 3 digit number :"))
# get first number in the list
first_int = number_list[0]
# get second number in the list
second_int = number_list[1]
# get third number in the list
third_int = number_list[2]
sorting_list = [0, 0, 0]
# find the middle method
# if first number is middle number
if (third_int < first_int < second_int) or (third_int > first_int > second_int):
    # put the number in the middle of sorting_list
    sorting_list[1] = first_int
    # put other 2 numbers in the right positions depends on < or >
    if third_int > first_int:
        sorting_list[2] = third_int
        sorting_list[0] = second_int
    else:
        sorting_list[2] = second_int
        sorting_list[0] = third_int
# if second number is middle number
elif (third_int < second_int < first_int) or (third_int > second_int > first_int):
    # put the number in the middle of sorting_list
    sorting_list[1] = second_int
    # put other 2 numbers in the right positions depends on < or >
    if third_int > second_int:
        sorting_list[2] = third_int
        sorting_list[0] = first_int
    else:
        sorting_list[2] = first_int
        sorting_list[0] = third_int
# if third number is middle number
else:
    # put the number in the middle of sorting_list
    sorting_list[1] = third_int
    # put other 2 numbers in the right positions depends on < or >
    if second_int > third_int:
        sorting_list[2] = second_int
        sorting_list[0] = first_int
    else:
        sorting_list[2] = first_int
        sorting_list[0] = second_int
print(sorting_list)

