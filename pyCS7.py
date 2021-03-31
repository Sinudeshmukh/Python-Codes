s = 'Welcome to the world of Python Programming'

lstwords = s.split()
print(lstwords)

result = [(index,item,len(item)) for index,item in enumerate(lstwords)]
print(result)