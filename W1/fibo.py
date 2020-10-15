def fibo(index):
    a, b = 1, 1
    print(a, end=" ")
    for i in range(index):
        a, b = b, a+b
        print(a, end=" ")
    print()


def fibo_v2(index):
    if index < 2:
        return 1
    return fibo_v2(index - 1) + fibo_v2(index - 2)


def fibo_print(index):
    for i in range(index):
        print(fibo_v2(i), end=" ")

    print()


print(fibo(500))
