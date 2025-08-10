# The merge_lists function takes two sorted lists as input and
# returns a new sorted list that contains all the elements from the input lists.
# However, there is a bug in this implementation that can cause it to produce incorrect output for certain inputs.

# Can you spot the bug and suggest a fix for it?

def merge_lists(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result += list1[i:]
    result += list2[j:]
    return result


if __name__ == '__main__':
    print(merge_lists([1, 3, 5, 7], [3, 4, 5, 6]))