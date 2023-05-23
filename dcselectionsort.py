def selectionsort(a):
     n = len(a)
     for i in range(n):
         min = i
         for j in range(i+1,n):
             if a[j]<a[min]:
                min=j
             temp=a[i]
             a[i]=a[min]
             a[min]=temp
x=[19,78,34,24,48,92,2]
print("Unsorted array is:",x)
selectionsort(x)
print("Sorted array is: ",x)
