def ispalindrome(s) :
    rev =''.join(reversed(s))
    if (s==rev):
        return True
    return False
s=input("enter the number")
ans= ispalindrome(s)
if(ans):
    print("true")
else:
    print("false")
