def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start+1, end-1)


arr = [1,2,3,4,5,6]
reverseArray(arr, 0, len(arr)-1)
print(arr)