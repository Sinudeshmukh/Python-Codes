# Fibonacci Series

n = int(input('Number'))


a, b = 0, 1
for item in range(n):
    print(a, end=' ')
    a, b = b, a+b


