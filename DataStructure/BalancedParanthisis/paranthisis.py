from DataStructure.utility import Stack
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        if symbol == ")":
            s.pop()
        else:
            if s.isEmpty():
                balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

z = str(input("enter the arithmetic expressions"))
print(parChecker(z))