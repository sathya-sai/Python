import random
head=0
tail=0
headpercent=0
tailpercent=0

for p in range(10):
    x=random.random()
    if x<=0.5:
        print('tail')
        tail += 1
    else:
        print('head')
        head += 1
headpercent=(head/10.0)*100
tailpercent=(tail/10.0)*100
print("Heads percent: " + str(headpercent))
print("Tail percent: " + str(tailpercent))




