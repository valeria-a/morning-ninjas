# Generators - a quick way to write iterators
# Generator function contains one or more yield statements.
#
# When called, it returns an object (iterator) but does not start execution immediately.
#
# Methods like iter() and next() are implemented automatically. So we can iterate through the items using next().
#
# Once the function yields, the function is paused and the control is transferred to the caller.
#
# Local variables and their states are remembered between successive calls.
#
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

# A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#     print("after first yield")
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n


# It returns an object but does not start execution immediately.
# a = my_gen()
#
# type(a)
#
# print(my_gen)
#
# # We can iterate through the items using next().
# val1 = next(a)
# # Once the function yields, the function is paused and the control is transferred to the caller.
# # Local variables and theirs states are remembered between successive calls.
# next(a)
# next(a)
# # Finally, when the function terminates, StopIteration is raised automatically on further calls.
# next(a)
#
# # or using for
# for i in my_gen():
#     print(i)


# A simple generator for Fibonacci Numbers
def fib(limit):

    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

# Create a generator object
x = fib(50)
for i in x:
    print(i)

# very efficient when handling a lot of data -
# no need to calculate everything at the beginning, just calculate one by one