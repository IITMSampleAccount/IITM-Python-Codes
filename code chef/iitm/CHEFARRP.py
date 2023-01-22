# cook your dish here
for t in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    for j in range(n+1):
        s,m = 0,1 
        
        for k in range(j,n):
            s=s+l[k]
            m=m*l[k]
            if s==m:
                c+=1  
    print(c)