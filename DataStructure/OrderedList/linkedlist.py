from DataStructure.utility import update, readfile, write, LinkedList
from pip._vendor.distlib.compat import raw_input
if __name__ == "__main__":
    list = LinkedList()
    word = readfile('data.txt')
for item in word:
    list.addnode(item)
print ("Current list is :")
list.disply()
val = raw_input("\nEnter a word to search:\n")
if list.search1(val):
    print ("Element found and deleting from the file\n")
    word.remove(val)
    list.delete1(val)
    write(word, 'data.txt')
    print(word)
else:
    print ("Element not found in a list\n")
    word.append(val)
    list.addnode(val)
    #list.sortlist(val)
    update(val, 'data.txt')
print ("File updated success:\n")
#list.sortlist()
list.disply()