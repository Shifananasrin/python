fact=int(input("enter the number"))
factors=[]
for i in range(1,fact+1):
    if fact%i==0:
        factors.append(i)
print( "factors of",fact,"is",factors)
