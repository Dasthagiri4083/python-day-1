s=input("s=")
t=input("t=")
count=0
n=0
l=0
k=0
for i in s:
    l=l+ord(i)
    count=count+1
for j in t:
        k=k+ord(j)
        n=n+1
if(count==n):
    if((l-k)%2==0):
        print("true")
    else:
        print("false")
else:
    print("false")
