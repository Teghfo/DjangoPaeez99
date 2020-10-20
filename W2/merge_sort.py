def merge_sort(arr):
    middle_len = len(arr) // 2

    if len(arr) > 1:
        left = arr[:middle_len]
        right = arr[middle_len:]

        left = merge_sort(left)
        right = merge_sort(right)
        arr = []
        print("left: ", left)
        print("right: ", right)
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                arr.append(right[0])
                right.pop(0)
            else:
                arr.append(left[0])
                left.pop(0)
        for elm in left:
            arr.append(elm)
        for elm in right:
            arr.append(elm)

    return arr


arr = [3, 5, 9, 1, 0, 10, 78, 125, -1, 0, 18]
print(arr)
print(merge_sort(arr))
