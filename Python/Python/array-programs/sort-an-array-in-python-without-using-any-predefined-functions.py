def bubbleSort(arr):
    swapped = True  # Initialize a flag to indicate if a swap has occurred

    # Continue until no swaps are made
    while swapped:
        swapped = False  # Reset the flag for each pass
        i = 0  # Initialize the index
        while True:
            print(swapped,'Rakesh');
            try:
                # Compare the current element with the next
                if arr[i] > arr[i + 1]:
                    # Swap the elements if they are in the wrong order
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True  # A swap was made
            except IndexError:
                break  # Exit the loop if the next index is out of bounds
            i += 1  # Move to the next index

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

bubbleSort(arr)  # Sort the array
print("Sorted array:", arr)
