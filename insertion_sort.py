def insertion_sort(array):
    #loop through the second element to the last
    for i in range(1, len(array)):
        #initialise element to position in its correct position
        key_element = array[i]

        #initialise variable to hold position of the reference key element

        j = i - 1

        #run through the iteration, find the correct position and shift the elements
        while j>=0 and array[j] > key_element:
            array[j+1] = array[j]
            j -= 1
            #position the key element in its right position
            array[j+1] = key_element
    
    return array

print(insertion_sort([8, 8, 6, 4, 5]))