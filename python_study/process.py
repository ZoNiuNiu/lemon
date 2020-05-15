import multiprocessing
import time

var = 0

def change_it(n):
    # 设为全局共享变量
    global var
    # time.sleep(1)
    for _ in range(10000000):
        var = var + n
        var = var + n

def run_thread(n):
    for i in range(3):
        change_it(n)

def print1():
    print(var)

if __name__ == "__main__":
    start_time = time.time()
    p1 = multiprocessing.Process(target = run_thread, args = (5,))
    p2 = multiprocessing.Process(target = run_thread, args = (8,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(time.time() - start_time)
    print1()

