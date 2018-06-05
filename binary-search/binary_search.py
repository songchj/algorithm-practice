def binary_search(src_list, item):
    low = 0
    high = len(src_list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = src_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

if __name__ == '__main__':
    print binary_search(my_list, 1)
    print binary_search(my_list, 3)
    print binary_search(my_list, 9)
    print binary_search(my_list, -1)
