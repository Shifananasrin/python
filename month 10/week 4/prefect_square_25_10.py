lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
print("Perfect squares:")
a=[]
for i in range(lower, upper + 1):
    j = int(i ** 0.5)
    if j * j == i:
     a.append(i)
print(a)

print("Even perfect squares:")
c=[]
for i in range(lower, upper + 1):
    j = int(i ** 0.5)
    if j * j == i and i % 2 == 0:
        c.append(i)
 print(c)
