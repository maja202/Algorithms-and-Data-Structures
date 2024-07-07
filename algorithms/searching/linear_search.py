def linear_search(arr, searched_val):
    for idx, val in enumerate(arr):
        if val == searched_val:
            return idx
            
    return -1
    
array = [2, 4, 0, 1, 9]
searched_val = 1

result = linear_search(array, searched_val)

if result == -1:
    print('Element not found')
else:
    print(f'Element found at index {result}')
