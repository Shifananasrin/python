
number_of_rows = 5

for i in range(1, number_of_rows + 1):

   # print(" " * (number_of_rows - i), end="")
    
    for j in range(1, i + 1):
     
        product = i * j
        print(product, end=" ")
   
    print()
