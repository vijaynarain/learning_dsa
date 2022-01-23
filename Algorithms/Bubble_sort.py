def bubbleSort(arr, n):
        # code here
        for i in range(n):
            #it's use to optimise the code, if our array is sorted already than we don't have to check again
            swapped = False 
            for j in range(n-i-1):
                if arr[j+1] < arr[j]:
                    swapped = True
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
            #if our array is sorted than break from loop and don't check again
            if swapped == False:
                break
        return arr
    
print(bubbleSort([4, 1, 3, 9, 7],5))
