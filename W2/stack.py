class Node:
    """
    Element in Stack
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Input: data
    Output: stack datastructure
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        node = Node(data)
        # if self.head == None:
        #     self.head = node
        # else:
        #     node.next = self.head
        #     self.head = node
        # self.length += 1

        node.next = self.head
        self.head = node
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def _pop(self):
        if self.is_empty():
            raise ValueError("Empty!")
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp.data

    def pop(self, rng=1):

        if isinstance(rng, list):
            rng = len(rng)

        res = []
        for i in range(rng):
            res.append(self._pop())
        print(f"removed_elemens: {res}")

    def __str__(self):
        stk = ""
        temp = self.head
        for i in range(self.length):
            stk += str(temp.data) + "-> "
            temp = temp.next
        return stk[:-3]


stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')
print(stack)
print("------------")
stack.pop(list(range(2)))
print(stack)
