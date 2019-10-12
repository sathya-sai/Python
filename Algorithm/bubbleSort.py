
# Driver code to test above
from Algorithm.utility import bubbleSort

arr = [str(input("Enter the elements \n"))]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])