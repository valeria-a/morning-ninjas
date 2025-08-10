def remove_duplicates(lst):
    unique = []
    for i in range(len(lst)):
        if lst[i] not in unique:
            unique.append(lst[i])
    return unique


if __name__ == '__main__':
    print(remove_duplicates([1,1,1,1,1]))