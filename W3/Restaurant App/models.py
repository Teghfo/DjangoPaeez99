import uuid
from abc import ABC, abstractmethod


class User:
    def __init__(self, email):
        self.email = email
        self.passw = uuid.uuid4()
        self.name = None
        self.age = None
        self.address = None

    def edit_profile(self, name=None, address=None, age=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if age:
            self.age = age

    def edit_passw(self, oldPass, newPassw) -> bool:
        if self.passw != oldPass:
            print("Boro kalak! old pass ro nemiduni")
            return False
        if len(newPassw) < 8:
            print("kamtar az 8 character nemishe")
            return False
        self.passw = newPassw
        return True

    def __str__(self):
        return self.name

# create food object using factory method


class FoodFactory(ABC):

    @abstractmethod
    def kitchen(self):
        pass


class ConcreteFood1(FoodFactory):
    def __init__(self):
        self.category = "Sonati"

    def kitchen(self):
        return Food1()


class ConcreteFood2(FoodFactory):
    def __init__(self):
        self.category = "FastFood"

    def kitchen(self):
        return Food2()


class ConcreteFood3(FoodFactory):
    def __init__(self):
        self.category = "deser"

    def kitchen(self):
        return Food3()


class FoodProduct(ABC):

    @abstractmethod
    def make(self):
        pass


class Food1(FoodProduct):
    def __init__(self):
        self.name = None

    def make(self, name):
        self.name = name
        print(f"{self.name} amadeh shod")


class Food2(FoodProduct):
    def __init__(self):
        self.name = None

    def make(self, name):
        self.name = name
        print(f"{self.name} amadeh shod")


class Food3(FoodProduct):
    def __init__(self):
        self.name = None

    def make(self, name):
        self.name = name
        print(f"{self.name} amadeh shod")


class Restaurant:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.uid = uuid.uuid4
        self.daily_menu = [[]]

    def get_uid(self):
        return self.uid

    def add_food(self, food, count):
        self.daily_menu.append([food, count])

    def find_food(self, food_name, count=1):
        for item in self.daily_menu:
            if item[0].name == food_name and item[1] >= count:
                return item
        return False

    def sell_food(self, food_name, count):
        food = self.find_food(food_name, count)
        if food:
            food[1] -= count
        else:
            raise ValueError("ghaza mojud nist!")
