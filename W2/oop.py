class A:
    count = 0
    name = 'khalil'

    # def __new__(cls):  # class method
    #     pass

    def __init__(self, name):  # instance method
        self.name = name
        A.count += 1

    def print_hello(self):
        print(f"hello, {self}")

    # def __str__(self):
    #     return self.name


# print(isinstance(A, object))
# print(issubclass(A, object))

# obj1 = A("ashkan")
# obj2 = A("asghar")
# obj3 = A("mammad")

# obj1.print_hello()

# print(A)


# print("type is instance object: ", isinstance(type, object))
# print("object is instance type: ", isinstance(object, type))
# print("object is subclass type: ", issubclass(object, type))
# print("type is subclass object: ", issubclass(type, object))
# print("object is instance object: ", isinstance(object, object))
# print("type is instance type: ", isinstance(type, type))
# print("type is subclass type: ", issubclass(type, type))


# def fibo(n):
#     f = [0] * n
#     f[0] = 1
#     f[1] = 1
#     for i in range(2, n):
#         f[i] = f[i - 1] + f[i-2]
#     return f[n-1]


# print(fibo(1000000))

class C:
    def __init__(self):
        pass


class B(C, A):
    """
    left is lady and lady is first

    """
    pass


class D(A):
    # override(extend)
    def print_hello(self):
        super().print_hello()  # extend
        print("hello in D")


# d = D("mamamd")
# d.print_hello()


#--------------------- new , init, call

class S:
    count = 0

    def __init__(self):
        self.name = "ashkan"
        print("in init")
        S.count += 1

    def __new__(cls, *args, **kwargs):
        if cls.count > 2:
            raise ValueError("Khak tu saresh!")
        return super().__new__(cls,  *args, **kwargs)

    def __call__(self):
        return "in call"


# s = S()
# s1 = S()
# s2 = S()
# s3 = S()
# print(s())


# --------------------- metaclass
class Meta(type):
    # def __new__(meta, name, bases, dct, *args, **kwargs):
    #     print('-----------------------------------')
    #     print("Allocating memory for class", name)
    #     print(meta)
    #     print(bases)
    #     print(dct)
    #     return super(Meta, meta).__new__(meta, name, bases, dct, *args, **kwargs)

    # def __init__(self, name, bases, dct, *args, **kwargs):
    #     self.name = 'Ashkan'
    #     super().__init__(name, bases, dct, *args, **kwargs)

    # def __call__(self, *args, **kwargs):
    #     print("in meta")
    #     return super().__call__(self, *args, **kwargs)

    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        # cls.name = "Ashkan"
        # x.name = 'Ashkan'
        print("in new Meta")
        return x

    def velemun_kon(self):
        print("khol shodim")


class E(metaclass=Meta):
    def __init__(self):
        print("in init E")

    def __new__(cls, *args, **kwargs):
        print("in new E")
        return super().__new__(cls,  *args, **kwargs)


# print(E.name)
# e = E()
# print(e.name)
# ---------------------
