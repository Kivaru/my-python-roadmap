from random import randint
from timeit import repeat

def bubble_sort(array):
    #size of the list
    n = len(array)

    for i in range(n):
        #flag to check if sort is done
        array_sorted = True

        #check each array item compare to its adjacent item, if greater swap
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                array_sorted = False
        if array_sorted:
            break

    return array


