import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def linearsearch(values,target):
    n=len(values)
    for i in range(n):
        if(values[i]==target):
            return True
    return False
values=[10,20,40,30,50,60,70,90,80]
target=8
if linearsearch(values,target):
    print("Target is found in the list")
else:
    print("Target is not in the list")
x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("Linear search time complexity is O(n)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
