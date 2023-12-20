
def isPossible(a, b, c, d):
    if c == a and d == b:
        return True
    elif a>c or b>d:
        return False
    else:
        return isPossible(a+b,b,c,d) or isPossible(a,b+a,c,d)

    return False



print(isPossible(1,4,62,45))
