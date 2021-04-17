def isPalindrome(s):
    s = s.lower()
    return s == s[::-1]





s = 'Malayalam'
print(isPalindrome(s))