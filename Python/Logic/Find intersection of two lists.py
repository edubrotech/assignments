##Find intersection of two lists
##Two-pointer logic (for sorted lists, no duplicates)

def sorted_intersection(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return result

print(sorted_intersection([1, 2, 3, 5, 7], [2, 3, 6, 7, 9]))
