# # ! /usr/bin/python
#
# from threading import Thread
# import time
#
# def my_counter():
#     i = 0
#     for _ in range(100000000):
#         i = i + 1
#     return True
#
#
# def main():
#     thread_array = {}
#     start_time = time.time()
#     for tid in range(2):
#         t = Thread(target=my_counter)
#         t.start()
#         t.join()
#     end_time = time.time()
#     print("Total time: {}".format(end_time - start_time))
#
#
# if __name__ == '__main__':
#     main()


# ! /usr/bin/python

from threading import Thread
import time


def my_counter(num):
    i = 0
    for _ in range(num):
        i = i + 1
    print(i)


def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter, args=(50000000 + 50000000 * tid,))
        print('start,i,{}'.format(tid))
        t.start()
        print('end,i,{}'.format(tid))
        thread_array[tid] = t
        print(thread_array)
    for i in range(2):
        print('start,i,{}'.format(i))
        thread_array[i].join()
        print('end,i,{}'.format(i))
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))


if __name__ == '__main__':
    main()