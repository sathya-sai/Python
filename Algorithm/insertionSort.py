from Algorithm.utility import insertionSort

arr = [12, 11, 13, 5, 6,-1]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]) 