def getprime(N, primeArr):  # Print prime or not
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeArr.append(num)

N = 1000
primeArr = []
getprime(1000, primeArr)        #calling prime function
blocks = []
k = 0
for i in range(0, 10):
    blocks.append([])
    min = k
    k = k + 100
    for j in primeArr:
        if  j <= k and j >= min:
            blocks[i].append(j)

for i in blocks:
    print (i)