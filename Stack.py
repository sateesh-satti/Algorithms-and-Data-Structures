class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def show(self):
        for i in self.items:
            print(i)


s= Stack()

print(s.isEmpty())

s.push("name")
s.push("age")
s.push("family")
s.push(20)
s.show()
print(s.peek())
