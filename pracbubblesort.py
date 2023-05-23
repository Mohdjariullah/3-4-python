"""import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")"""
def bubblesort(seq):
    n=len(seq)
    for i in range(n-1):
        for j in range(n-1):
            if seq[j]>seq[j+1]:
                temp=seq[j]
                seq[j]=seq[j+1]
                seq[j+1]=temp
seq=[10,2300,320,401,503,805,70,80,90,1]
print("Before sorting:",seq)
bubblesort(seq)
print("after sorting:",seq)
"""
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Bubble sort time complexity is O(n)")
plt.xlabel("Input")
plt.ylabel("time")
plt.show()"""
