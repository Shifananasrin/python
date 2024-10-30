n=int(input("enter the number:"))
a,b=0,1
print("fibnocci series is:")
for i in range(n):
    print(a, end=' ')
    a,b= b,a+b
