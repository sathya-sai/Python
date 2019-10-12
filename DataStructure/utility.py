# FOR UNORDERED AND ORDERED*******************************************************************************

def readfile(fl):
    with open(fl, 'r') as File:  # open file in read mode
        lst = File.read().split()  # Read File and store in list
    File.close()
    return lst


def update(word, fl):
    f = open(fl, "a")  # open file file in append mode
    f.write(" %s " % word)  # write the word in file
    f.close()


def write(list, fl):
    f = open(fl, 'w')  # Open File In write mode
    for item in list:
        f.write("%s " % item)  # Write in the file
    f.close()


class Node:  # class to create node for a list
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:  # linked list class /link list operational class
    def __init__(self):
        self.head = None

    def addnode(self, data):  # adding new node
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            tempnode = self.head
            while tempnode.next is not None:
                tempnode = tempnode.next
            tempnode.next = newnode
            return True

    def disply(self):  # displaying nodes which present in a list
        tempnode = self.head
        if tempnode is None:
            print("List is empty")
            return False
        while tempnode.next is not None:
            print(tempnode.data, " ", )
            tempnode = tempnode.next
        print(tempnode.data, " ", )

    def search1(self, data):  # Seaching for the node to find string equal or not
        self.disply()
        tempnode = self.head
        print(data)
        while tempnode is not None:
            if tempnode.data == data:
                return True
            tempnode = tempnode.next
        return False

    def delete1(self, data):  # delete node in a list
        prvnode = tempnode = self.head
        if tempnode.data == data:
            self.head = tempnode.next
        else:
            while tempnode.data != data:
                prvnode = tempnode
                tempnode = tempnode.next
            prvnode.next = tempnode.next


# deque for palindrome *******************************************************************************

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addF(self, item):
        self.items.append(item)

    def addR(self, item):
        self.items.insert(0, item)

    def removeF(self):
        return self.items.pop()

    def removeR(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# Stack functions for Balanced Parentheses****************************************************************8

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Queue abstract data types for Simulate Banking Cash Counter************************************************

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dqueue(self):
        if self.isEmpty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def disp(self, val):
        print(val)


# for Calender Program****************************************************************

class Calender:

    def day(self, d, m, y):  # finding the day of week
        y1 = y - ((14 - m) / 12)
        x = y1 + y1 / 4 - y1 / 100 + y1 / 400
        m1 = m + 12 * ((14 - m) / 12) - 2
        d1 = (d + x + ((31 * m1) / 12)) % 7
        return d1

    def week(self, week):
        for i in week:
            print(i, end=' ')

    def leapyear(self, year):  # check weather year leap year or not
        if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
            return True
        else:
            return False


# Bianary Search Tree&*********************************************************
def number_of_binary_trees(n: int):
    """
    This function is for count the no of possible binary trees in given no

    """
    try:
        count = [0 for i in range(n + 1)]
        count[0] = count[1] = 1
        # initialising count to one for zero and one

        i = 2
        for i in range(2, n + 1):
            # iterate loop from 2 to n+1
            for j in range(i):
                # iterate loop till range of i
                count[i] += count[j] * count[i - j - 1]
                # counting no of possible binary trees

        return count[i]
        # returning count
    except ValueError:
        print("wrong values")
    except IndexError:
        print("traversing in out of index")
