string = input("enter the list")
word=input("enter the word in list to search:")
c = []
count=0
c = string.split(" ")
for i in range(0,len(c)):
        if (word==c[i]):
                count=count+1
	
print("count of the word is:",count)
