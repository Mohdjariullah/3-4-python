import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
def insertion_sort(a):
    n=len(a)
    for i in range(1,n-1):
        k=a[i]
        j=i-1
        while(j>=0 and a[j]>k):

            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
a=[34,46,43,22,57,71,45,57,90]
print("Before sorting:",a)
insertion_sort(a)
print("After sorting:",a)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Selection sort Time Complexity is O(n\400b2)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()
