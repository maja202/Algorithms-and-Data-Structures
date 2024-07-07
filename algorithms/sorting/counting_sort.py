def counting_sort(arr, n):
    max_val = arr[0]
    
    for val in arr:
        if val > max_val:
            max_val = val
            
    counts = [0] * (max_val + 1)
    
    for i in range(n):
        counts[arr[i]] += 1
        
    for i in range(1, max_val + 1):
        counts[i] += counts[i - 1]
        
    output = [0] * n
    
    for i in range(n - 1, -1, -1):
        counts[arr[i]] -= 1
        output[counts[arr[i]]] = arr[i]
        
    for i in range(n):
        arr[i] = output[i]
        
data_to_sort = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data_to_sort, len(data_to_sort))

print("Array sorted in ascending order: ")
print(data_to_sort)
