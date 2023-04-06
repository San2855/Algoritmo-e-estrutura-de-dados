def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for elem in arr:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    print(arr)
    return quicksort(left) + [pivot] + quicksort(right)
      
arr = [3, 7, 1, 9, 2, 6, 8, 5, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)

