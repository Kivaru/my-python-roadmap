def merge(left, right):
    #if the first array is empty, then deal with second and vice versa
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    result = []
    index_left=index_right = 0

    #loop through the arrays until all the elements make it to the result array

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left =+ 1
        else:
            result.append([index_right])
            index_right =+ 1

        #add the remaining elements to the result array at the end of the loop and break the loop

        if index_left == len(left):
            result += left[index_left:]
            break
        if index_right == len(right):
            result += right[index_right:]
            break
    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    left = array[:midpoint]
    right = array[midpoint:]

    return merge(left, right)

merge_sort([8, 2, 6, 4, 5])