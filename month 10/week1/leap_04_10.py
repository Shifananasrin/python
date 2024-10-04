leapYear=int(input("enter the year"))
for year in range(2024,leapYear+1):
    if(year%4==0 and year%100!=0) or(year%400==0):
        print("yes!it is leap year",year)
    else:
        print("no! it is  not leap year",year)
 
