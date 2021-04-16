# Fibonacci Series
# Fib(0) = 0
# Fib(1) = 1
# Fib(2) = Fib(1) + Fib(0) = 1 + 0 = 1
# Fib(3) = Fib(2) + Fib(1) = 1 + 1 = 2

# Fib(5) = Fib(4) + Fib(3) = 3 + 2 = 5

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 ....

lookup = {}


def fibo(n):
    if n == 0 or n == 1:
        lookup[n] = n

    if n not in lookup:
        lookup[n] = fibo(n-1) + fibo(n-2)

    return lookup[n]


num = int(input('Enter a Number: '))


for item in range(num+1):
    print(fibo(item), end=' ')