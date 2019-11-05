def selection_sort_udemy(arr):
    for i in range(len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if i != smallest_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
