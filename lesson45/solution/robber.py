def robber(l: list) -> int:
    if len(l) == 0:
        return 0

    if len(l) == 1:
        return l[0]

    return max(l[0] + robber(l[2:]), l[1] + robber(l[3:]))


if __name__ == '__main__':
    print(robber([2, 7, 9, 3, 1]))
    print(robber([1, 2, 3, 1]))
    print(robber([5, 1, 1, 5]))
    print(robber([5, 1, 1, 5, 10]))
    print(robber([7, 1, 1, 6, 1, 7]))

    [7, 1, 1, 6, 1, 7]

