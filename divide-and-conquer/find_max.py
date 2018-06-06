def max(list, num):
    if list == []:
        return None
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        num = list[0]
        if num < list[1]:
            num = list[1]
        return num
    return max(list[1:], list[0])

def standard_max(list):
    if list == []:
        return None
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = standard_max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

list1 = []
list2 = [1]
list3 = [1, 2]
list4 = [3, 4, 2, 5, 7]

print max(list1, None)
print max(list2, None)
print max(list3, None)
print max(list4, None)
print "#"*20
print standard_max(list1)
print standard_max(list2)
print standard_max(list3)
print standard_max(list4)