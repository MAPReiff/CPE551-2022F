import time


def timer(func, *args):
    start = time.time()
    for i in range(100000):
        func(*args)
    return time.time() - start


a = timer(pow, 2, 4)
print("finished", a)

b = timer(str.upper, 'spam')
print("finished", b)