"""
Program 3 :

Using  Python lambda function to  create a Fibonacci series from 1 to 50 element 
"""
def fibonacci_series(n):
    # Initialize the first two numbers of the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to n elements
    while len(fib_sequence) < n:
        # Append the sum of the last two numbers in the sequence
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Generate Fibonacci series with 50 elements
fib_series = fibonacci_series(50)

# Print the series
print(fib_series)

