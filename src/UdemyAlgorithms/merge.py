def merge_sort(nums):
    if len(nums) == 1:
        return

    middle_index = len(nums) // 2

    left = nums[:middle_index]
    right = nums[middle_index:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        nums[k] = right[j]
        k += 1
        j += 1

arr1 = [4,5,2,3,7,6,8,9,1,2,6,5,4]
merge_sort(arr1)
print(arr1)
