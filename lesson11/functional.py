# function as an object

# def foo_power(num1, num2):
#     return num1 ** num2
#
# print(foo_power(3, 4))
#
# my_func_variable = foo_power
#
# type(foo_power)
#
# foo_power.__name__
#
#
# my_func_variable(3,4)



# Now you can pass function as any variable as a param

# def foo_sum(num1, num2):
#     return num1 + num2
#
# def operation_on_numbers(op, num1, num2):
#     return op(num1, num2)
#
# print(operation_on_numbers(foo_sum, 5, 6))
#
# print(operation_on_numbers(foo_power, 5, 6))