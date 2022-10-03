def sumsquare(l):
    esum=0
    osum=0
    for i in l:
        if(i%2==0):
            esum=esum+i*i
        else:
            osum=osum+i*i
    print("[",osum,",",esum,"]")
n=int(input("enter the number of elements:"))
l=[]
for i in range(n):
    m=int(input("enter the elements:"))
    l.append(m)
sumsquare(l)
