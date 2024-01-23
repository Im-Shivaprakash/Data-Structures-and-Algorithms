def merger(arr, start, mid, end):
    
    ls = mid - start + 1
    rs = end - mid
    
    la = arr[start:start+ls]
    ra = arr[mid+1:mid+ls+1]

    i = j = 0
    k = start

    while i < ls and j < rs:
        
        if la[i] < ra[j]:
            arr[k] = la[i]
            i+=1
            
        else:
            arr[k] = ra[j]
            j+=1
        
        k+=1
    
    while i < ls:

        arr[k] = la[i]
        i+=1
        k+=1

    while j < rs :

        arr[k] = ra[j]
        j+=1
        k+=1

def mergeSort(arr, start, end):
    if start < end:                      #head_recursion
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merger(arr, start, mid, end)
    
    return arr

input_array = list(map(int, input().split()))
n = len(input_array)
result = mergeSort(input_array, 0, n-1)
print(result)5 4 3 2 1 0