
# Driver code to test above
from Algorithm.utility import bubbleSort

arr = [64, 34, 25, 128, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])