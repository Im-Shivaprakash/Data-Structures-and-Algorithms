def partition(arr, low, high):
    pivot = arr[high]
    pi = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[pi] = arr[pi], arr[j]
            pi+=1
    arr[pi], arr[high] = arr[high], arr[pi]
    return pi

def QuickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)

arr = [6,2,4,7,5,1,3]
n = len(arr)
QuickSort(arr, 0, n-1)
print(arr)