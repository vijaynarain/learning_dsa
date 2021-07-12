"""
Sort an Array using Quicksort algorithm
example:-
arr = {11, 2, 4, 5, 10, 3, 45}
"""

def partition(start, end, array):

    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):

    if (start < end):

        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

if __name__ == "__main__":
  
  array = [11, 2, 4, 5, 10, 3, 45]
  print(f"UnSorted array: {array}")
  quick_sort(0, len(array) - 1, array)
  print(f'Sorted array:   {array}')
