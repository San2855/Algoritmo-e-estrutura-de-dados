def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        # Encontra o menor elemento restante na lista
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troca o menor elemento com o primeiro elemento restante na lista
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [3, 7, 1, 9, 2, 6, 8, 5, 4]
sorted_arr = selectionsort(arr)
print(sorted_arr)