son = {'d':2}
father = [{'a':1, 'b':{'c':1, 'd':2}},{'f':1}]

# for item in list1:
#      a = list(item.values())
#      for item1 in a:
#          print (item1)
#          if type(item1) == dict:
#              print(list(item1.items()))

import operator
son_list = list(son.items())

def new_father_list(mid_list):
    for list_item in mid_list:
        a = list(list_item.items())
        print(a)
        father_list = []
        for item1 in a:
            if type(item1[1]) == dict:
                print(item1[1])
            else:
              father_list.append(item1)



new_father_list(father)


# if operator.le(son_list,son_list):
#     print(True)