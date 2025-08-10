def digital_root(n: int) -> int:
    if n < 10:
        return n
    else:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        return digital_root(sum_digits)


if __name__ == '__main__':
    print(digital_root(192834))
