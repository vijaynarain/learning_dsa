"""
Print all possible combinations of r elements in a given array of size n

Given an array of size n, generate and print all possible combinations of r elements in array. For example, if input array is {1, 2, 3, 4} and r is 2, then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.
"""
def printCombination(arr, n, r):
 
    # A temporary array to store
    # all combination one by one
    data = [0] * r
 
    # Print all combination using
    # temporary array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)
 
''' arr[] ---> Input Array
n     ---> Size of input array
r     ---> Size of a combination to be printed
index ---> Current index in data[]
data[] ---> Temporary array to store
            current combination
i     ---> index of current element in arr[]     '''


def combinationUtil(arr, n, r, index, data, i):
 
    # Current cobination is ready,
    # print it
    if (index == r):
        for j in range(r):
            print(data[j], end = " ")
        print()
        return
 
    # When no more elements are
    # there to put in data[]
    if (i >= n):
        return
 
    # current is included, put
    # next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1)
 
    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)
 
# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    r = 3
    n = len(arr)
    printCombination(arr, n, r)
 