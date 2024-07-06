def selection_sort(arr):
    for i in range(0, len(arr)):
        min_val_id = i
        for j in range(i + 1, len(arr)):
            if arr[min_val_id] > arr[j]:
                min_val_id = j
                
        arr[i], arr[min_val_id] = arr[min_val_id], arr[i]
        
data_to_sort = [-2, 45, 0, 11, -9]
selection_sort(data_to_sort)

print('Array sorted in ascending order:')
print(data_to_sort)
