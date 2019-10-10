
from pip._vendor.distlib.compat import raw_input

from DataStructure.utility import readfile, write, update, LinkedList

if __name__=="__main__":
    list = LinkedList()
    word = readfile('text.txt')
for item in word:
    list.addnode(item)
print("Current list is :")
list.disply()
val = raw_input("\nEnter a word to search:\n")
if list.search1(val):
    print("Element found and deleting from the file\n")
    word.remove(val)
    list.delete1(val)
    write(word,'text.txt')
else:
    print("Element not found in a list\n")
    word.append(val)
    list.addnode(val)
    update(val,'text.txt')          #updating string into file
print("File updated success:\n")
list.disply()