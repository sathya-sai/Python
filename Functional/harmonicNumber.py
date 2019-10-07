result=0
num=1
num=int(input('enter the number'))
for n in range(num):
    result = result + 1 / num
    num-=1
print('result'+str(result))