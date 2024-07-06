def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, right, mid)
    
def merge(arr, left, right, mid):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i, j = 0, 0
    k = left
    
    while i < mid - left + 1 and j < right - mid:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1    
        
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
        
    return arr
    
data_to_sort = [6, 5, 12, 10, 9, 1]

merge_sort(data_to_sort, 0, len(data_to_sort) - 1)

print("Array sorted in ascending order: ")
print(data_to_sort)
