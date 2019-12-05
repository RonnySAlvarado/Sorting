# TO-DO: Complete the selection_sort() function below
# [4, 10, 8, 2, 12, 6]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


print(selection_sort([4, 10, 8, 2, 12, 6]))


# TO-DO:  implement the Bubble Sort function below

# [4, 10, 8, 2, 12, 6]
# Funny enough, the bubble sort method is something I learned when we were going through JS for the first time. When we weren't allowed to use the .sort() method, this is what I had done
def bubble_sort(arr):
    for number in range(len(arr)-1):
        for unsorted in range(len(arr)-1):
            if arr[unsorted] > arr[unsorted + 1]:
                temp = arr[unsorted + 1]
                arr[unsorted + 1] = arr[unsorted]
                arr[unsorted] = temp
    return arr


print(bubble_sort([4, 10, 8, 2, 12, 6]))


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
