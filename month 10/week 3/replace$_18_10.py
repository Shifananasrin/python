string = input("Type a string : ")
modified_string= string[0]+string[1:].replace(string[0],'$')

print("modified string is:",modified_string)
