def getprime (N, primeArr):
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeArr.append(num)

def Prime_anagram (primearr):
    print("The Prime anagram values are")
    for i in primearr:
        primearr.remove(i)
        for j in primearr:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j):
                anagrams.append(i)
                anagrams.append(j)
                print (i)




class Node:  # Node class
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack:  # class to make stack operation
    def __init__ (self):
        self.head = None

    def isEmpty (self):
        return self.items == []

    def push (self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node = self.head
            self.head = new_node

    def pop (self):  # Deleting elements from the stack
        if self.head is None:
            return None
        else:
            popping = self.head.data
            self.head = self.head.next
            return popping



N = 1000
primeArr = []
blocks = []

getprime(N, primeArr)  # generating prime numbers
primearr = primeArr  # taking refrence of primenumbers to check wether they are anagrams or not
anagrams = []

Prime_anagram(primearr)
st = Stack()
print("Anagram in reverse Order\n", anagrams)  # Printing prime numbers
for a in anagrams:
    st.push(a)
    a = int(a)

