from Algorithm.utility import Prime_anagram, primearr, anagrams

Prime_anagram(primearr)
print("Anagram prime numbers are\n", anagrams)

print("The Palindrome Prime are:\n")
a = 0
b = 1000
a += 1
for i in range(a,b):
    if(str(i) == str(i)[::-1]):
        if(i>2):
            for a in range(2,i):
                y = True
                if(i%a==0):
                    y = False
                    break
            if y:
                print(i)