# mutable vs immutable arguments

# returning multiple values as tuple

# optional arguments (default values)

# *args
# def a(*argv):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)

# a('Hello', 'Welcome', 'to', 'Python', 'Class')
# a()

# def a1(argv):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)

#a1(4,5)
#
# def b(required_param, *argv):
#     print ("First argument :", required_param)
#     for arg in argv:
#         print("Next argument through *argv :", arg)

# b('Hello', 'Welcome', 'to', 'Python', 'Class')

# b()

# def c(**kwargs):
#     print(type(kwargs))
#     print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

# c(first ='Python', mid ='Full', last='Stack')
# c()
# c("Pyton")


# def d(arg1, **kwargs):
#     print(f"arg1: {arg1}")
#     print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

# d(5, first="Hello", second="Bye")
# d(first="abc")
# d(5, 'Hello')

#
#
# def d(*args, **kwargs):
#     print(f"args num: {len(args)}, args: {args}")
#     print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

# d(5, 10, first='abc', second='def')
# d()
# d(first='abc', 5)

# **kwargs