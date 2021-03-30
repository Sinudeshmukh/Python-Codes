s = 'Welcome to the world of Python Programming'


# split

lstwords = s.split()


result = []
for item in lstwords:
    result.append((item,len(item)))

print(result)

# Using LC
results = [(item, len(item)) for item in lstwords]
print(results)