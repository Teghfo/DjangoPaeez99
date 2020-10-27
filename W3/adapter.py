from abc import ABC, abstractmethod


class Target(ABC):
    """
    define abstract method that implement in concrete adapter
    """
    @abstractmethod
    def operation(self):
        pass


class Adaptee:

    def specific_opertation(self):
        return "in Adaptee, JSON"


class Adapter(Target, Adaptee):

    def operation(self):
        print(f"in adapter XML To {self.specific_opertation()}")


def client(target):
    target.operation()


if __name__ == "__main__":
    target = Adapter()
    client(target)
