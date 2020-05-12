import operator

# Test

son = {'d': 2}
father = [{'a': 1, 'b': {'c': 1, 'd': 2}}, {'f': 1}]

son_list = list(son.items())


def change(abc):
    mid_list = []
    for item1 in abc:
        if type(item1[1]) == dict:
            two_list = list(item1[1].items())
            for list_item in two_list:
                mid_list.append(list_item)
        else:
            mid_list.append(item1)
    return mid_list


father_list = []
for item in father:
    b = change(list(item.items()))
    father_list = father_list + b

print(son_list)
print(father_list)
print(set(son_list))
print(set(father_list))

if set(son_list).issubset(set(father_list)):
    print(True)
else:
    print(False)

"""
请编写Python函数，判断一个字典（单层结构）是否是某json（考虑字典和列表嵌套的情况）的子集，
入参1中所有key-value都在入参2中出现。如果是，则返回True，否则返回False。
示例1：入参1：｛'d':2｝入参2：[{'a':1,'b':{'c':1,'d':2}},{'f':1}]返回值：True
示例2：入参1：｛'d':2,'f':2｝入参2：[{'a':1,'b':{'c':1,'d':2}},{'f':1}]返回值：False
"""
