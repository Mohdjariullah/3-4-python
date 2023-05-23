import time #to check time taken for execution
class stack:
    def __init__(self):
        self.items=[]
    def empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def display(self):
        return(self.items)
S=stack()
Start=time.time()#syncs time
print(Start)#print time
print(S.empty())
print("push operation")
S.push(11)
S.push(12)
S.push(54)
S.push(13)
print(S.display())
print("Size: ",S.size())
print("Peek: ",S.peek())
print("Pop operation")
print(S.pop())
S.push(67)
S.push(79)
print(S.size())
print(S.display())
print("size: ",S.size())
end=time.time()#end time
print(end)#pritn time

b=end-Start
print(b)
