List=input("enter the list:")
L=[int(x) for x in List.split(" ")]

print("the list is",L)
while True:  
    print("\nMAIN MENU")  
    print("1.Greater and Lower Number")  
    print("2. Sorting")
    print("3. Even number list")
    print("4. Exit")  
    choice = int(input("Enter the Choice:"))
    if choice == 1:
         print("the greatest number is:",max(L))
         print("the greatest number is:",min(L))
    elif choice == 2:
         print("the sorted list is",sorted(L))
    elif choice == 3:
             even=[n for n in L if n % 2 == 0]
             print("the even list is",even)
    elif choice == 4:
        print("exit")  
        break
    else:
         print("\n invalid")
