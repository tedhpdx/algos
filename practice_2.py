#count inversions


def mergeSort(arr, n):
    #initialize temp array
    temp_arr = [0]*n
    starting_left_index = 0
    rightmost_index = n-1
    return _mergeSort(arr, temp_arr, starting_left_index, rightmost_index)

def _mergeSort(arr, temp_arr, left_index, right_index):
    inversion_count = 0
    #this must be the case, or there are no more elements
    if left_index < right_index:
        #split the array in to 2 subarrays
        middle_index = (left_index+right_index)//2
        #count inversions in left subarray
        inversion_count += _mergeSort(arr, temp_arr, left_index, middle_index)
        #count inversions in right subarray
        right_side_of_middle_index = middle_index + 1
        inversion_count += _mergeSort(arr, temp_arr, right_side_of_middle_index, right_index)
        #merge two subarrays
        inversion_count += merge(arr, temp_arr, left_index, middle_index, right_index)
    return inversion_count

def merge(arr, temp_arr, left_index, middle_index, right_index):
    #start of left subarray
    i = left_index
    #start of right sub array
    right_side_of_middle = middle_index + 1
    j = right_side_of_middle
    k = left_index
    merge_inversion_count = 0

    #keep i and j in within their limits
    while i <= middle_index and j <= right_index:
        #no inversion
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        #yes inversion because now arr[i] > arr[j]
        #j is always larger than i so that's an inversion        #
        else:
            temp_arr[k] = arr[j]
            #so for this position we know that a[i] will be larger than all others after it
            merge_inversion_count += (middle_index-i+1)
            k += 1
            j += 1

    #copy remaining elements of left subarray into temp array
    while i <= middle_index:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    #copy remaining elements of right subarray into temp array
    while j <= right_index:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    # Copy the sorted subarray into Original array
    for loop_var in range(left_index, right_index + 1):
        arr[loop_var] = temp_arr[loop_var]

    return merge_inversion_count











arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print(result)