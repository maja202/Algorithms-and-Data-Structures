def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
                
    return arr
    
data_to_sort = [3, -5, 1, 0, 4, 3, -8]
insertion_sort(data_to_sort)

print('Array sorted in ascending order:')
print(data_to_sort) 
