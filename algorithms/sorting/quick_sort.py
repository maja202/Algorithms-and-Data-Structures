def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right) 
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot, right)
        
        
def partition(arr, left, right):
    pivot = arr[right]
    idx = left
    
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
            
    arr[right], arr[idx] = arr[idx], arr[right]

    return idx
    
data = [8, 7, 2, 1, 0, 9, 6]
quick_sort(data, 0, len(data) - 1)

print('Array sorted in ascending order:')
print(data)
