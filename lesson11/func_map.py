# map(func, *iterables) --> map object
# def foo_squared(num):
#     return num**2
#
# my_list = [1, 3, 5, 6]
#
# ret_val = map(foo_squared, my_list)
#
# type(ret_val)
#
# print(ret_val)
#
# # print(ret_val[0])
#
# for i in ret_val:
#     print(i)

# print(next(ret_val))
# print(next(ret_val))

# you can also pass multiple iterators to map
# def foo_sum(num1, num2):
#     return num1 + num2
# my_tuple1, my_tuple2 = (1, 2, 3, 4), (10, 20, 30, 40)
# ret_val = map(foo_sum, my_tuple1, my_tuple2)
# print(list(ret_val))

# we want any number of params
# def s(*args):
#     ret_val = 0
#     for a in args:
#         ret_val += a
#     return ret_val
#
# ret_val = map(s, my_tuple1, my_tuple2, (100, 200, 300, 400))
# print(list(ret_val))

# you can pass any existing function, or functions defined in class (method)
# example - map to upper case
# ret_val = map(str.upper, ['a', 'bb', 'ccc'])
# ret_val = map(lambda x: x.upper(), ['a', 'bb', 'ccc'])
# ret_val = []
# for i in ['a', 'bb', 'ccc']:
#     ret_val.append(i.upper())
# print(list(ret_val))