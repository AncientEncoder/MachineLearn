def is_palindrome(x):
    tmp = x
    revX = 0
    while(x > 0):
        getNum = x % 10
        revX = revX*10+getNum
        x = x//10
    if tmp == revX:
        return "YES"
    else:
        return "NO"