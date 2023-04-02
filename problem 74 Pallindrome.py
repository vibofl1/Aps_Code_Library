

def isPallindrome(N):
        a=bin(N).replace("0b", "")
        if a==a[::-1]:
            return True
        else:
            return False
isPallindrome(45)