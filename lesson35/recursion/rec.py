def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def factorial_while(n):
    res = 1
    while n >= 1:
        res = n * res
        n = n-1
    return res


def rec_factorial(n):
    if n == 1:
        return n
    return n * rec_factorial(n-1)


def print_numbers_desc(n):
    while n >= 0:
        print(n, end=" ")
        n = n-1


def print_numbers_rec(n):
    if n == -1:
        return
    print(n, end=" ")
    print_numbers_rec(n-1)


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)




if __name__ == '__main__':
    # print(fib(10))
    # print_numbers_rec(10)
    # print(rec_factorial(3))
    pass
