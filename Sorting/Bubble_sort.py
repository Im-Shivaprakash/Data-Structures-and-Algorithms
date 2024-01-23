def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        is_swapped = False      #Flag 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if not is_swapped :
            break
    return arr
    
arr = list(map(int, input().split()))
result = bubble_sort(arr)
print(result)

#Can also do it using counter
