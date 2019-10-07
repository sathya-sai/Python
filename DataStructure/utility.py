def readfile (fl):
    with open(fl, 'r') as file:
        lst = file.read().split()
        file.close()
    return lst

def update (word, fl):
    f = open(fl, "a")
    f.write("%s" %word)
    f.close()

def write(list, fl):
    f = open(fl, 'w')
    for item in list:
        f.write("%s" %item)
    f.close()

def search(self, data):
    self.display()
    tempnode = self.head
    print(data)
    while tempnode is not None:
        if tempnode.data == data:
            return True
        tempnode = tempnode.next
    return False

#deque
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


#Stack functions for Balanced Paranthisis
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    #def peek(self):
        #return self.items[len(self.items) - 1]

    #    def size(self):
       # return len(self.items)
