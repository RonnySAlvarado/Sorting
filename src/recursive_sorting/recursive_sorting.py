# # TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO

#     return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# With help of PT4 lecture around 1:10:00 to 1:30:00
def partition(data):
    left = []
    pivot = data[0]
    right = []
    for val in data[1:]:
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)
    return left, pivot, right


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    left, pivot, right = partition(arr)
    return merge_sort(left) + [pivot] + merge_sort(right)


print(merge_sort([6, 5, 4, 3, 2, 1]))
print(merge_sort([3, 5, 6, 1, 4, 2]))
# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
