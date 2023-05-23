#Insertion search
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def insertion(seq):
    n=len(seq)
    for i in range(1,n-1):
        k=seq[i]
        j=i-1
        while(j>=0 and seq[j]>k):
            seq[j+1]=seq[j]
            j=j-1
            seq[j+1]=k
lis=[34,46,24,78,53,45,21,70,58]
print("Before sorting:",lis)
insertion(lis)
print("After sorting:",lis)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Isnsertion sort time complexity ")
plt.xlabel("TIme")
plt.ylabel("input")
plt.show()
