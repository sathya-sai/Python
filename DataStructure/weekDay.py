from DataStructure.utility import Queue

q = Queue()
# input for the queue
wee = ['SUN', 'MON', 'TUE', 'WED', 'THUR', 'FRI', 'SAT']
a = ['SUN', 1, 8, 15, 22, 29]
b = ['MON', 2, 9, 16, 23, 30]
c = ['TUE', 3, 10, 17, 24, 31]
d = ['WED', 4, 11, 18, 25, ' ']
e = ['THU', 5, 12, 19, 26, ' ']
f = ['FRI', 6, 13, 20, 27, ' ']
g = ['SAT', 7, 14, 21, 28, ' ']
# pushing the elements into queuee
q.enqueue(a)
q.enqueue(b)
q.enqueue(c)
q.enqueue(d)
q.enqueue(e)
q.enqueue(f)
q.enqueue(g)
# displaying the elements
q.disp(a)
q.disp(b)
q.disp(c)
q.disp(d)
q.disp(e)
q.disp(f)
q.disp(g)
# poping the elements from the queue
q.dqueue()
q.dqueue()
q.dqueue()
q.dqueue()
q.dqueue()
q.dqueue()
q.dqueue()
