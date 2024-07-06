def bubble_sort(array):
    array_len = len(array)

    for i in range(array_len):
        for j in range(array_len - i - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]

    
data_to_sort = [-30, 41, 0, 11, -9, 0, 12, -8]
bubble_sort(data_to_sort)

print('Array sorted in ascending order:')
print(data_to_sort)
