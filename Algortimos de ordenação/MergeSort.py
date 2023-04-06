def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)
    
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


arr = [3, 7, 1, 9, 2, 6, 8, 5, 4]
sorted_arr = mergesort(arr)
print(sorted_arr)