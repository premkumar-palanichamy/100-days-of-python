## Additional

def ReplaceElements(arr, n):
    prod = 1


    for i in range(n):
        prod *= arr[i]
    for i in range(n):
        arr[i] = prod // arr[i]


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)

    ReplaceElements(arr, n)

    # Print the modified array.
    for i in range(n):
        print(arr[i], end=" ")




lst = "aaaaabbbbwwwrre"
x = a
def countX (lst, x):
    count = 0
    for value in lst:
        if (value ==x):
            count = count + 1
    return count
print (countX)