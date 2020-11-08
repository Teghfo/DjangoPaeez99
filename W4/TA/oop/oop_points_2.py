def add(x, y):
    return x + y


a = add
b = 4
c = 5


def sub(x, y):
    return x - y


def operate(func, x, y):
    result = func(x, y)
    return result


# print(operate(a, b, c))


def simple_print():
    print('i like to print something')


def operate_v2(func):
    def inner():
        print('this print related to inner func')
        func()

    return inner


v2_operate = operate_v2(simple_print)


# print(type(v2_operate))


@operate_v2
def simple_print_v2():
    print('i like to print something')


v3_operate = simple_print_v2


# print(type(v3_operate))


# v2_operate()
# print(v2_operate)


class A:
    @staticmethod
    def print_simple():
        print(' skjdflksdjflsdj ')

    @staticmethod
    def assumption_func2():
        return 5 + 6


# def divide(a, b):
#     return a / b
#
#
# print(divide(8, 0))
#
# def divide_decorator(func):
#     def inner():
#         func()
#         return
#     return inner
#
# @divide_decorator
# def divide(a, b):
#     return a / b
#
# print(divide(8, 0))

def divide(a, b):
    return a / b

def divide_decorator(func):
    def inner(x, y):
        if y == 0:
            return ('you do not have permission to divide')
        else:
            return func(x, y)

    return inner



@divide_decorator
def divide(a, b):
    return a / b

print(divide(8,0))
# print(divide(8,3))
# print(type(divide))
# print(divide(8, 0))
# print(divide(8, 2))
