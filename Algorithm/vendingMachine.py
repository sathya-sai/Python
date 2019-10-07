def countCurrency(amount):
    notes = [2000, 500,200,100,50,20,10,5,2,1]
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Currency Count ->")
    for i,j in zip(notes, noteCounter):
        if amount >=1:
            j = amount // i
            amount = amount -j * i
            print(i, ":", j)
amount = int(input("Enter amount"))
countCurrency(amount)
