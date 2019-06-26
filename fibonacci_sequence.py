### In mathematics, the Fibonacci numbers, commonly denoted Fn form a sequence,
## called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
# starting from 0 and 1.

### f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
