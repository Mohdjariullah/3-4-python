#selection sort
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def selectionsort(seq):
    n=len(seq)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if seq[j]<seq[min]:
                temp=seq[min]
                seq[min]=seq[j]
                seq[j]=temp
seq=[56,53,32,66,21,78,965,64,2,54,2]
print("Before sorting:",seq)
selectionsort(seq)
print("After sorting:",seq)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Selection sort time compleity is O(n)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
