def binary_search(arr, target):
    """
    Binary search on a sorted array.
    Returns the index of target if found, otherwise -1.
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
    
    return -1


def linear_search(arr, target):
    """
    Linear search on an array.
    Returns the index of target if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1


# Example usage
if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    
    target = 23
    print(f"Linear search for {target}: {linear_search(numbers, target)}")
    print(f"Binary search for {target}: {binary_search(numbers, target)}")
    
    target = 100
    print(f"Linear search for {target}: {linear_search(numbers, target)}")
    print(f"Binary search for {target}: {binary_search(numbers, target)}")