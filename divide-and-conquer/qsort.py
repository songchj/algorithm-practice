def qsort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot ]
        greater = [i for i in list[1:] if i > pivot ]
        return qsort(less) + [pivot] + qsort(greater)

list1 = [1]
list2 = [3, 1]
list3 = [1, 4, 3, 2, 7]

print qsort(list1)
print qsort(list2)
print qsort(list3)