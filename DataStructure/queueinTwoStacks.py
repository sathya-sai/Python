class Queue:
    def __init__ (self):
        self.queue = []

    def enqueue (self, val):
        self.queue.insert(0, val)
        print("push in q=1",val)

    def dequeue (self):
        print("pop from q=1", self.queue.pop())

    def size (self):
        return len(self.queue)

    def disp (self, val):
        print (val)

class Stack:
    def __init__ (self):
        self.items = []

    def isEmpty (self):
        return self.items == []

    def push (self, data):
        self.items.append(data)
        print("push in Stack",data)

    def pop (self):
        print("pop in Stack",self.items.pop())

    def size (self):
        return len(self.items)

    def disp (self, data):
        print (data)


st = Stack()
st2 = Stack()
q2 = Queue()
a = ['SUN', 1, 8, 15, 22, 29]
b = ['MON', 2, 9, 16, 23, 30]
c = ['TUE', 3, 10, 17, 24, 31]
d = ['WED', 4, 11, 18, 25, ' ']
e = ['THU', 5, 12, 19, 26, ' ']
f = ['FRI', 6, 13, 20, 27, ' ']
g = ['SAT', 7, 14, 21, 28, ' ']

q2.enqueue(a)
q2.enqueue(b)
q2.enqueue(c)
q2.enqueue(d)
q2.enqueue(e)
q2.enqueue(f)
q2.enqueue(g)

q2.dequeue()
st.push(a)
q2.dequeue()
st.push(b)
q2.dequeue()
st.push(c)
q2.dequeue()
st.push(d)
q2.dequeue()
st.push(e)
q2.dequeue()
st.push(f)
q2.dequeue()
st.push(g)

st.pop()
st2.push(g)
st.pop()
st2.push(f)
st.pop()
st2.push(e)
st.pop()
st2.push(d)
st.pop()
st2.push(c)
st.pop()
st2.push(b)
st.pop()
st2.push(a)

print('\n************STACK_OBJECTS************************\n')
st2.pop()
st2.pop()
st2.pop()
st2.pop()
st2.pop()
st2.pop()
st2.pop()