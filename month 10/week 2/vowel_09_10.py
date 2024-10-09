string = input( "Typ in a string: " )
vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
n = ""

for i in string:
    if i in vowels:
        n += i
print( "vowels in ",string ,"are",n )
