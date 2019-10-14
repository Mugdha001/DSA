print("Insertion Sort")
arr = [64,25,12,22,11]
minIndex = 0
#consider 1st element to be a part of sorted array
for i in range(1,len(arr)):
    #check if any element to left is less than element at i
    if arr[i]>arr[i-1]:
        continue
    for j in range(0,i):
        if arr[i]<arr[j]:
            minIndex = j 
            temp = arr[i]
            break
    for j in range(i,minIndex,-1):
        arr[j]= arr[j-1]
    arr[minIndex]=temp
        
#print(arr)