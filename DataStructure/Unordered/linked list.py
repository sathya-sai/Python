from DataStructure.utility import update, readfile, write


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def addnode(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            tempnode = self.head
            while tempnode.next is not None:
                tempnode = tempnode.next
            tempnode.next = newnode

    def display(self):
        tempnode = self.head
        if tempnode is None:
            print('List is Empty')
            return
        while tempnode.next is not None:
            print(tempnode.data)
            tempnode = tempnode.next
        print(tempnode.data)


if __name__ == "__main__":
    list = Linkedlist()
    word = readfile('text.txt')
for item in word:
    list.addnode(item)
print('the current list is:')
list.display()
val = str(input('Enter the word to search\n'))
if list.search(val):
    print('Element found and deleting from the file')
    word.remove(val)
    list.delete(val)
    write(word, 'list.txt')
else:
    print('element not found in the list\n')
    word.append(val)
    list.addnode(val)
    update(val, 'text.txt')
print('file updated sucessfully\n')
list.display()
