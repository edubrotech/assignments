def find_missing_number(arr, n):
    xor_all = 0

    for i in range(1, n + 1):
        xor_all ^= i
        print("xor_all-------------",xor_all)
    print(xor_all)
    for num in arr:
        print("num====",num,xor_all)

        xor_all ^= num
        print("xor_all================",xor_all)

    return xor_all

arr = [1, 2, 4, 5]
n = 1
print(find_missing_number(arr, n))