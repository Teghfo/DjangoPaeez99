class Person():
    age = 30
    address = 'tehran'

    def __init__(self, sex):
        self.sex = sex

    def print_age(self):
        print(self.age)

    @staticmethod
    def print_age_static():
        print(Person.age)


    @classmethod
    def print_age_class(cls):
        print(cls.age)


a = Person
a.print_age_class()
a.print_age_static()

# person1 = Person('male')
# person1.print_age()
#
# print(Person.add(5, 30))
