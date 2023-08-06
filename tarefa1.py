def fibonacci_count(limit):
    fib_sequence = [1, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    print( "sequencia" , fib_sequence )

    count = 0
    for num in fib_sequence:
        if 1 <= num <= 100:
            count += 1
    return count

result = fibonacci_count(100)
print("Number of Fibonacci numbers between 1 and 100:", result)

