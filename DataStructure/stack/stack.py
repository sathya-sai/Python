class stack:
    def __init__(self):
        self.item = list()
        self.size = 5
        self.top = 0

    def __set__(self):
        self.item = []

    def input_fun(self):
        while (True):
            ch = int(input("1-push\n2-pop\n3-Disply\n4-quit\nEnter choice\n"))
            st.switch(ch)

    def isEmpty(self):
        if self.top <= 0:
            return True
        else:
            return False

    def push(self,data):
        self.item.append(data)
        self.top += 1

    def pop(self):
        if st.isEmpty():
            print("NO elements in stack")
        else:
            val=self.item.pop()
            self.top-=1
            return val

    def disp(self):
        if st.isEmpty():
            print("NO elements in stack")
        else:
            print("Elements are:")
            for i in range(len(self.item)):
                print(self.item[i])

    def quit(self):
        print("Invalid choice\n")
        return

    def switch(self, ch):
        if ch == 1:
            if self.top == self.size:
                print("Stack is full !..")
            else:
                e = int(input("Enter val to push\n"))
                st.push(e)
        if ch == 2:
            if st.isEmpty():
                print ("Stack is empty")
            else:
                print ("Popped value: "), st.pop()
        if ch == 3:
            st.disp()
        if ch == 4:
            st.quit()

if __name__ == "__main__":
    st = stack()
    st.input_fun()