def binary_search(arr, left, right, searched_val):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        
        if arr[mid] == searched_val:
            return mid
            
        if arr[mid] > searched_val:
            return binary_search(arr, left, mid - 1, searched_val)
        else:
            return binary_search(arr, mid + 1, right, searched_val)
        
array = [0, 2, 6, 9, 11, 12]
searched_val = 12

result = binary_search(array, 0, len(array), searched_val)

if result == -1:
    print('Element not found')
else:
    print(f'Element found at index {result}')
