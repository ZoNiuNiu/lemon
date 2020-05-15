import time, threading

var = 0
lock = threading.Lock()

def change_it(n):
    # 设为全局共享变量
    global var
    # time.sleep(1)
    for _ in range(10000000):
        var = var + n
        var = var + n

def run_thread(n):
    for i in range(3):
        # 先要获取锁:
        # time.sleep(1)
        lock.acquire()
        print("第%d次循环，n=%d   " % (i, n))
        change_it(n)
        # 改完了一定要释放锁:
        lock.release()
        print("释放锁第%d次循环，n=%d   " %(i, n))

start_time = time.time()
t1 = threading.Thread(target=run_thread, args=(5,)) # 逗号不能省！
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print(time.time() - start_time)
print(var)