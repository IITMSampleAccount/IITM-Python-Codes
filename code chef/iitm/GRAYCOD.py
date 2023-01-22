# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    l=["0", "1"]
    for i in range(n-1):
        l1=[]
        l2=[]
        for i in l:
            l1.append("0"+i)
        for j in l[::-1]:
            l2.append("1"+j)
        l=l1+l2
    for k in l:
        print(int(k,2), end=" ")
    print()
    t=t-1

