# Iterative Binary Search
def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid  # Element found
        elif arr[mid] < x:
            low = mid + 1  # Ignore the left half
        else:
            high = mid - 1  # Ignore the right half
    return -1  # Element not found

# Recursive Binary Search
def binary_search_recursive(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid  # Element found
        elif arr[mid] < x:
            return binary_search_recursive(arr, mid + 1, high, x)  # Search the right half
        else:
            return binary_search_recursive(arr, low, mid - 1, x)  # Search the left half
    return -1  # Element not found

# Example usage
arr = [2, 3, 4, 10, 40]
x = 40

# Iterative Search
result_iterative = binary_search_iterative(arr, x)
print(f"Iterative: Element found at index {result_iterative}" if result_iterative != -1 else "Iterative: Element not found")

# Recursive Search
result_recursive = binary_search_recursive(arr, 0, len(arr) - 1, x)
print(f"Recursive: Element found at index {result_recursive}" if result_recursive != -1 else "Recursive: Element not found")
