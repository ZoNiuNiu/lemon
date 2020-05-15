# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
#
# g = foo()
# print(next(g))
# print("*"*10)
# print(next(g))
# print("*"*20)
# print(next(g))



# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()
# print(gr1.dead)
# print(gr2.dead)

from greenlet import greenlet

def test1(x, y):
    z, x = gr2.switch(x+y)
    print('test1 ', z, x)

def test2(u):
    print('test2 ', u)
    gr3.switch()

def test3():
    print('test3')
    gr1.switch(10, 'opo')

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr3 = greenlet(test3)
# print(gr1.switch("hello", " world"))
gr1.switch("hello", " world")

print(gr1.dead)
print(gr2.dead)
print(gr3.dead)