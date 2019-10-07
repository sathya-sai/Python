import time

a=int(input("Enter 1 to start"))
if a == 1:

    s =str(time.time())

    for i in range(len(s)):
        b = int(input("enter 2 to stop"))
        if b == 2:
            break
        print(i)

    end = time.time()
    c = end - float(s)
    print(c)
else:
    print("invalid")