print([x for x in range(10) if x%2 == 1])

my_text = 'i love you, i love sxt, i love you'

a = {c:my_text.count(c) for c in my_text if my_text.count(c)>1}
print(a)