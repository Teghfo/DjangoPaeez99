class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0  # Optional

    def add_begin(self, elm):
        if self.root == None:
            self.root = elm
        else:
            elm.next = self.root
            self.root = elm
        self.length += 1

    def add_end(self, elm):
        pass

    def add_between(self, elm0, newelm):
        pass

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

l = LinkedList()
l.add_begin(elm1)
l.add_begin(elm2)

print(l)
