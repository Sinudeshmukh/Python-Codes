#Factorial of  a number

def iterFactorial(num):
    result = 1
    for item in range(1,n+1):
        result = result * item

    return result

n = int(input('Enter number'))

output = iterFactorial(n)
print("Factorial of {} is {}".format(n, output))
