
list=input("enter the list")
Name=list.split()
print("the name of list is\n", Name)
count=0
for i in Name:
    
        count+=i.lower().count('a')
 

print("occurance of a ", count)
