def quick_sort(arr, low, high):
    if low >= high: return

    pivot = partition(arr, low, high)
    quick_sort(arr, pivot+1, high)
    quick_sort(arr, low, pivot-1)

def partition(arr, low, high):
    pivot_index = (low+high)//2
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low
    for j in range(low, high):
        if arr[j]<= arr[high]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[high], arr[i] = arr[i], arr[high]
    return i

arr1 = [0,5,3,7,8,4,1,34,2,6,78,3,4,5,7,8,13,25]
quick_sort(arr1, 0, len(arr1)-1)
print(arr1)