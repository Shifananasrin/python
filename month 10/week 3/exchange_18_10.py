string=input("enter the list")
if(len(string)>1):
   string=string[-1]+string[1:-1]+string[0]
print(string)
