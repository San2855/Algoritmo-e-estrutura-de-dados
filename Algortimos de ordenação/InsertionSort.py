def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        # Armazena o valor do elemento atual
        key = arr[i]
        # Move os elementos maiores que key para uma posição a frente
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        # Insere key na posição correta
        arr[j+1] = key
    return arr

arr = [3, 7, 1, 9, 2, 6, 8, 5, 4]
sorted_arr = insertionsort(arr)
print(sorted_arr)