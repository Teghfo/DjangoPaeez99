class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0  # Optional

    def __increment_length(self):
        self.length += 1

    def add_begin(self, elm):
        if self.root == None:
            self.root = elm
        else:
            elm.next = self.root
            self.root = elm
        self.__increment_length()

    def add_end(self, elm):
        if self.root == None:
            self.root = elm
        else:
            temp = self.root
            while temp.next != None:
                temp = temp.next
            temp.next = elm
        self.__increment_length()

    def add_between(self, elm0, newelm):
        temp = self.root
        find_flag = False

        while True:
            if temp is elm0:
                find_flag = True
                break
            elif temp.next == None:
                break
            temp = temp.next

        if find_flag:
            newelm.next = temp.next
            temp.next = newelm
        else:
            raise "Not Found"

    def pop_elm(self):
        pass

    def del_elm(self, elm):
        pass

    def insert(self, elm, index):
        pass

    def __str__(self):
        if self.root == None:
            return "Linked List is empty!"
        print(self.root.data)
        temp = self.root
        while temp.next != None:
            print(temp.next.data)
            temp = temp.next
        return "Done!"


elm1 = Element("Khalil")
elm2 = Element("Alireza")
elm3 = Element("Niloufar")

l = LinkedList()
l.add_begin(elm2)
l.add_begin(elm1)
l.add_between(elm1, elm3)
print(l)
