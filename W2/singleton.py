# class MySingleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance


# a = MySingleton()
# b = MySingleton()


# print(id(a))
# print(id(b))


class Meta(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance

        print(Meta._instance)
        return cls._instance[cls]


class MySingleton1(metaclass=Meta):
    pass


class MySingleton2(metaclass=Meta):
    pass


obj11 = MySingleton1()
obj12 = MySingleton1()
obj21 = MySingleton2()
obj22 = MySingleton2()


print(id(obj11))
print(id(obj12))
print(id(obj21))
print(id(obj22))
