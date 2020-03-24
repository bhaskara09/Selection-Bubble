def bubbleSort(arr): 
    n = len(arr) 
  
    for i in range(n): 
  
        for j in range(0, n-i-1): 
  
            
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
arr = [60, 29, 31, 85, 20, 2, 4, 18, 38] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  
