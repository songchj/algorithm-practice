def find_smallest(arr):
    smallest_value = arr[0]
    smallest_index = 0
    for index, value in enumerate(arr):
        if value < smallest_value:
            smallest_index = index
    return smallest_index

def selection_sort(arr):
    result = []
    while arr:
        index = find_smallest(arr)
        result.append(arr.pop(index))
    return result


if __name__ == '__main__':
    print selection_sort([5, 3, 6, 2, 10])