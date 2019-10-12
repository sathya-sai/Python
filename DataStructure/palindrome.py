from pip._vendor.distlib.compat import raw_input
from DataStructure.utility import Deque
q = Deque()
wrd = raw_input("Enter a word to check to Palindrome\n")
for i in wrd:
    q.addF(i)
while len(q.items) > 1:
    a = q.removeF()  # traversing each character from BOTH front and rare end
    b = q.removeR()
    if a == b:
        print()  # deleting element from double end if the charecters are same
    else:
        break
if q.isEmpty() == True or q.size() == 1:
    print("Palindrome")  # printing if its palindrome
else:
    print( "Not Palindrome")

