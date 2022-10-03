def happy(n):
    k=0
    l=n
    while(n>0):
        b=n%10
        k=k+b**2
        n=n//10
    if(k==1):
        print("true")
    elif(k==l*l):
        print("false")
    else:
        return happy(k)
n=int(input("n="))
if(n>0):
    happy(n)
else:
    print("false")
