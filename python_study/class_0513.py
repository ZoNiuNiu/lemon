import random

total = 0
for i in range(10):
    投资金额 = 1
    # 0 是小 ， 1 是大
    while 1-random.randint(0,1):
        lose = 投资金额
        投资金额 *= 2
        total -= lose

    get = 投资金额
    total += get

print(total)
