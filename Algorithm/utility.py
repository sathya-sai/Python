def binary_search(alist, key):
    """Search key in alist[start... end - 1]."""
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end) // 2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1





def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n  - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Driver code to test above

def countCurrency(amount):
    notes = [2000, 500,200,100,50,20,10,5,2,1]
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Currency Count ->")
    for i,j in zip(notes, noteCounter):
        if amount >=1:
            j = amount // i
            amount = amount -j * i
            print(i, ":", j)
#For anagram prime amd Palindrome
N = 1000
primeArr = []
blocks = []
def getprime (N, primeArr):
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

def Prime_anagram (primearr):
    for i in primearr:
        primearr.remove(i)
        for j in primearr:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j):
                anagrams.append(i)
                anagrams.append(j)
                print (i)
