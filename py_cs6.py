

# def mysquare(num):
#     return num * num
#
#
# print(mysquare(9))


f = lambda num: num * num
result = f(5)
print("Square of Number", result)
print(f)
print(type(f))

# print("Square of Number", (lambda num: num*num)(10))
# print("Square of Number",lambda num:num*num(int(input("Enter a Number"))))

fun = lambda x, y: x if x> y else y
print("Max of X,y", fun(3,5))
