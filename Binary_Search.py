def binary_search(arr, target):
    """
    Perform binary search to find the index of the target in a sorted array.

    Args:
        arr (list): The sorted array in which to search.
        target: The value to find in the array.

    Returns:
        int: The index of the target in the array if found, -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found in the array

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")
