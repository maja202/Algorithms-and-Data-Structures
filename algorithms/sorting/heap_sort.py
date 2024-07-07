def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        
        heapify(arr, i, 0)
        
def heapify(arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    
    if left < n and arr[largest] < arr[left]:
        largest = left
        
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)
        
data_to_sort = [1, 12, 9, 5, 6, 10]
heap_sort(data_to_sort)

print("Array sorted in ascending order:")
print(data_to_sort)
