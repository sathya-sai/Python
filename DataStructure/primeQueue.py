from DataStructure.utility import Queue
N = 1000
primeArr = []
blocks = []


def getprime (N, primeArr): #for prime
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeArr.append(num)


getprime(N, primeArr)
primearr = primeArr
anagrams = []


def Prime_anagram (primearr): #for prime anagram
    for i in primearr:
        primearr.remove(i)
        for j in primearr:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j):
                anagrams.append(i)
                anagrams.append(j)
                print (i)


Prime_anagram(primearr)
q = Queue()
print("Anagram prime numbers are\n", anagrams)

print("Anagarams in reverse order")
reverse = []
for i in anagrams:
    reverse.append(i)
    i = q.dqueue()

reverse.sort(reverse=True)
print(reverse)

