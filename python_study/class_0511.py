print([x for x in range(10) if x%2 == 1])

my_text = 'i love you, i love sxt, i love you'

a = {c:my_text.count(c) for c in my_text if my_text.count(c)>1}
print(a)


def print_max(xa,xb):
    if xa>xb:
        print(xa,'较大值')
    else:
        print(xb,'较大值')
    print(id(xa))

print_max(10,20)
