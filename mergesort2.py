#function to divide the list into two sublists
def merge_sort(list, left_index, right_index):
    if left_index >= right_index:
        return 
        
    middle = (left_index + right_index)//2
    merge_sort(list, left_index, middle)
    merge_sort(list, middle+1, right_index)
    merge(list, left_index, right_index, middle)

#function to merge the sublists into one sorted list

def merge(list, left_index, right_index, middle):
    #creating subparts of a list
    left_sublist = list[left_index:middle+1]
    right_sublist = list[middle+1:right_index+1]

    #indeces initial values
    left_sublist_index = right_sublist_index = 0
    sorted_index = left_index

    #traversing through the list
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
        #if left sublist has smaller element, put it into the sorted
        #then move forward in the left sublist
        if left_sublist[left_sublist_index] < right_sublist[right_sublist_index]:
            list[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        else:
            list[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1
        
        #move forward in the sorted part
        sorted_index = sorted_index + 1

    #traverse through the remaining elements and add them up
    while left_sublist_index < len(left_sublist):
        list[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1
    
    while right_sublist_index < len(right_sublist):
        list[sorted_index] = right_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

list = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]  
merge_sort(list, 0, len(list)-1)  
print(list)
    

    

