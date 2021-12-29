def nextPermutation(N,arr):
    # code here
    idx = -1
    for i in range(1,N):
        if arr[idx-1] < arr[idx]:
            #print(arr[idx-1])
            break
        idx = idx - 1
    chota = idx - 1 #3
    
    for i in range(len(arr[idx-1:-1])):
        #print(arr[idx+i])
        if arr[idx] > arr[chota]:
            if arr[idx] < arr[idx-1]:
                bada = idx
            idx = idx + 1
    arr[chota],arr[bada] = arr[bada],arr[chota]
    
   # for i in range(len(arr[chota:-1])):
    #    if arr[pointer-1] > arr[pointer]:
     ##  pointer = pointer + 1
       
    i = -1
    start = chota + 1
    while start < i:
        arr[start],arr[i] = arr[i],arr[start]
        start = start + 1
        i = i - 1
    
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3]
    N = len(arr)
    print(arr)
    print(nextPermutation(N,arr))

"""
1. fistly we have to traverse the list from end side
2. if we get end-1 < end, than we have the store the index of end-1
3. now we traverse from end+1 to end of the list and find out which value is passes this case "value > end-1(which we store the value) and value < value-1(index)"
like end-1 = 3, 5 > 3 and 5 < 6
4. after traversing whole list we have to swipe the value which we get in the end "arr[chota],arr[bada] = arr[bada],arr[chota]" like 3 to 4
5. now we have to reverse the list from end+1 to end of the list
like:- 4,6,5,3 == 4,3,5,6
6. return result
"""
