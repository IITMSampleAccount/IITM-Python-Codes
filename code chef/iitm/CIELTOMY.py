

def check(k,n,x1,d,g):
    if k==n:
        x1+=[d[n]]
        return
    for i in range(1,n+1):
        if g[k][i]!=0 and d[i]==-1:
            d[i]=d[k]+g[k][i]
            check(i,n,x1,d,g)
            d[i]=-1
for i in range(int(input())):
    v,e=map(int,input().split())
    g=[[0 for i in range(11)]for j in range(11)]
    for i in range(e):
        x,y,w=map(int,input().split())
        g[x][y]=w
        g[y][x]=w
    x1=[]
    d=[-1]*(v+1)
    d[1]=0
    check(1,v,x1,d,g)
    x1.sort()
    r=x1[0]
    s=0
    for i in range(len(x1)):
        if r==x1[i]:
            s+=1
    print(s)