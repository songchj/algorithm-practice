# -*- coding: utf-8 -*-
#自己写的
def sum_list(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    else:   
        return l.pop(0) + sum_list(l)

#参考答案
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print sum_list(list1)
print sum(list2)