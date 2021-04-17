# Write a Program to check whether string is palindrome or not

#Madam
#Malayalam

# m a l a y a l a m
# 0 1 2 3 4 5 6 7 8

def isPalindrome(s):
    s = s.lower()
    for item in range(len(s)//2):
        if s[item] != s[len(s) - item - 1]:
            return False
    return True

s = 'Malayalam'
print(isPalindrome(s))