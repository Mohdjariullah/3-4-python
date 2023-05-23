import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def linearsearch(thevalues,target):
    n=len(thevalues)
    for i in range(n):
        if thevalues[i]==target:
            return True     
    return False
thevalues=[10,20,50,60,70,80,90]
target=200
if linearsearch(thevalues,target):
    print("target value is found in list")
else:
    print("target value is not found in list")
x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("linearsearch line complexity is o (o)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
