def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[19,78,34,76,24,48,92,2]
print("Unsorted array is:",a)
bubblesort(a)
print("Sorted array is: ",a)
