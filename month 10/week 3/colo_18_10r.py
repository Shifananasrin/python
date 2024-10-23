count = int(input("How much colors :"))
colors=[]

for i in range(count):
    
    colors.append(input("Color : "))
print("list of color is",colors)
print("first color in list  and  second color in list",[colors[0],colors[-1]])


