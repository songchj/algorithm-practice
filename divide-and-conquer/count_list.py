def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


list1 = []
list2 = [1]
list3 = [1, 2, 3, 4]

print count(list1)
print count(list2)
print count(list3)