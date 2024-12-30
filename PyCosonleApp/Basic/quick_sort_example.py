def quick_sort(arr):
    # Base case: an array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here, the last element)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot
    # Recursively sort the left and right partitions, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
numbers = [10, 7, 8, 9, 1, 5]
print("Original list:", numbers)

sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
