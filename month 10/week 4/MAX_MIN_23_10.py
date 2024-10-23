number=input("enter element into list")
L=[]
for n in number:
    L.append(int(n))
print("the list is",L)
print ("the maximum value of list is:",max(L))
print ("the minimum value of list is:",min(L))
print ("the length of  the list:",len(L))

print ("the sum of  the list:",sum(L))
Sort=sorted(L)
print ("the sorted of  the list:",Sort)
Sort.reverse()
print ("the reverse of  the list:",Sort)
