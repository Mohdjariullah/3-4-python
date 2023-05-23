import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
def selection_sort(seq):
    n=len(seq)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if seq[j]<seq[min]:
                temp=seq[min]
                seq[min]=seq[j]
                seq[j]=temp
seq=[10,70,15,8,90,20]
print("Before sorting:",seq)
selection_sort(seq)
print("After sorting:",seq)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Selection sort Time Complexity is O(n\400b2)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()
