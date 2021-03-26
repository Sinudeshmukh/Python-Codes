# Factorial

def recurFactorial(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num * recurFactorial(num -1)


n = int(input('Enter number'))

output = recurFactorial(n)
print("Factorial of {} is {}".format(n, output))
