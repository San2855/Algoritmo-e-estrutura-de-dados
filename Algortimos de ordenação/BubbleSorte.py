def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos já estão no lugar certo
        for j in range(n-i-1):
            # Percorre a lista de 0 até n-i-2
            if arr[j] > arr[j+1]:
                # Troca os elementos adjacentes se estiverem na ordem errada
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr


arr = [3, 7, 1, 9, 2, 6, 8, 5, 4]
sorted_arr = bubblesort(arr)
