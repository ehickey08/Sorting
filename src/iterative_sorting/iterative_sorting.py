#done in class
def insertion_sort (arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j>0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = temp
    return arr

# TO-DO: Complete the selection_sort() function below
def selection_sort ( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]: smallest_index = j

        if i != smallest_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # TO-DO: swap

    return arr
# TO-DO:  implement the Bubble Sort function below
def bubble_sort ( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

    return arr

# STRETCH: implement the Count Sort function below
def count_sort ( arr, maximum=-1 ):
    return arr
