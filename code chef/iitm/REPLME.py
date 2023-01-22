# cook your dish here
a=int(input())
ar=[]
for i in range(1,a+1):
    x=int(input())
    ar.append(x)
ar.sort()
for i in range(len(ar),1,-1):
    d=ar[0]
    e=ar[1]
    ar.remove(d)
    ar.remove(e)
    ar.append(((3*d)+(2*e))%100)
    ar.sort()
print(ar[0])