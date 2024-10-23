num=input("enter the number").split()
for i in range(len(num)):
       
    if  int (num[i])>=100:
        num[i]="over"
print("number list:",num)
