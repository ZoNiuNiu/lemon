import threading, time

start_time = time.time()
def fgg(a):
    time.sleep(a)

def run(n, num):
    print("{0},Begin".format(n))
    fgg(num)
    print("{0},end".format(n))

t1 = threading.Thread(target=run, args=("th1", 2))
t2 = threading.Thread(target=run, args=("th2", 4))

t1.start()
t2.start()
t1.join()
t2.join()

print(time.time() - start_time)