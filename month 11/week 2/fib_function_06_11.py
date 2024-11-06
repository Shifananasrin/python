def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series is:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers

# Get input from the user
n = int(input("Enter the number: "))

# Call the function to print the Fibonacci series
fibonacci_series(n)
