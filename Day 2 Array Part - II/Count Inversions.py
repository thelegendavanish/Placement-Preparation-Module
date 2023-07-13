from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getInversions(arr, n):
    # Variable to store the total inversions in the list.
    totalInversions = 0

    # Check for each element whether any smaller element is present on right side.
    for i in range(n) :
        for j in range (i+1, n) :
            if (arr[i] > arr[j]) :
                totalInversions += 1

    return totalInversions

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))