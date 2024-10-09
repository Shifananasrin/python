LIST=input("enter the list:")
L=[]
for n in LIST:
    L.append(n)
print("Before swappin in the list")
print(L)
L[0],L[-1]=L[-1],L[0]
print("After swapping in the list")
print(L)
