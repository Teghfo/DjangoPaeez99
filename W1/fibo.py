import time


def fibo(index):
    a, b = 1, 1
    for i in range(index):
        a, b = b, a+b
    return a


cache = {}


def fibo_cache(n):
    if n not in cache.keys():
        cache[n] = fibo_v2(n)
        print(cache)
    return cache[n]


def fibo_v2(index):
    if index < 2:
        return 1
    return fibo_cache(index - 1) + fibo_cache(index - 2)


def fibo_print(index):
    for i in range(index):
        print(fibo_v2(i), end=" ")

    print()


m = 10
start = time.time()

print(fibo(m))

done = time.time()

print("fibo mamuli:", done - start)

start = time.time()

print(fibo_v2(m))

done = time.time()

print("fibo recursive:", done - start)
