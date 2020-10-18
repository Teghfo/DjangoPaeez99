
sample_array = [3, 5, 11, 22, 45, 83, 101, 102]


# Returns index of x in arr if present, else -1
def recursive_binary_search(input_array, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        if input_array[mid] == x:
            return mid

        elif input_array[mid] > x:
            return recursive_binary_search(input_array, low, mid - 1, x)

        else:
            return recursive_binary_search(input_array, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


print(recursive_binary_search(sample_array, 0, len(sample_array) - 1, 102))
#
#
# def iterative_binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#
#     while low <= high:
#
#         mid = (high + low) // 2
#
#         # Check if x is present at mid
#         if arr[mid] < x:
#             low = mid + 1
#
#         # If x is greater, ignore left half
#         elif arr[mid] > x:
#             high = mid - 1
#
#         # If x is smaller, ignore right half
#         else:
#             return mid
#
#             # If we reach here, then the element was not present
#     return -1
#
#
# print(iterative_binary_search(sample_array, 102))
