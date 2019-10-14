from DataStructure.utility import Queue

q = Queue()
cash = 2000  # Intial ammount in cash counter
while True:
    ch = int(input("1-Deposit\n2-Withdraw\n3-Exit \n4-Display_amount\n"))  # asking user input
    if ch == 1:
        q.enqueue(1)  # deposits method
        amnt = int(input("Enter amount Deposit\n"))
        if amnt > 0:
            cash += amnt
            print("Amount Deposit success")
            q.enqueue(amnt)  # amount pushing into queue
        else:
            print("enter valid amount")


    elif ch == 2:  # withdraw metho
        amnt = int(input("Enter amount Withdraw"))
        if amnt > 0:
            if amnt <= cash:
                cash -= amnt
                q.enqueue(amnt)  # pooping amount from the queue
                print("Amount withdraw success")
            else:
                print("Sorry no enough balance")
        else:
            print("Enter valid amount")

    elif ch == 4:
        print("current amount is =", cash)  # displaying current amount
    else:
        quit()
