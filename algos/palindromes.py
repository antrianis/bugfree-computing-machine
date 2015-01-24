def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[len(s) - 1]:
        return False
    return True and palindrome(s[1:(len(s) - 1) ])

print palindrome('aibohphobia')
print palindrome('hello')
print palindrome('kayak')
