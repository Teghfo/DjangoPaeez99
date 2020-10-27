from abc import ABC, abstractmethod


class InternetInterface(ABC):
    @abstractmethod
    def operation(self, ip):
        pass


class RealInternet(InternetInterface):

    def operation(self):
        print(f"Hoooray! welcome!")


class Proxy(InternetInterface):

    def __init__(self, ip):
        self.ip = ip

    blocked_ip = ['iran', 'cuba', 'china', 'russia', 'north korea']

    def operation(self):
        if self.ip in Proxy.blocked_ip:
            print(
                f"sorry {self.ip}!!")
            return
        real_internet = RealInternet()
        real_internet.operation()


def client(InternetInterface):

    InternetInterface.operation()


if __name__ == "__main__":
    print("connection from proxy!")
    connection = Proxy('iran')
    client(connection)

    print("direct connection!")
    connection = RealInternet()
    client(connection)
