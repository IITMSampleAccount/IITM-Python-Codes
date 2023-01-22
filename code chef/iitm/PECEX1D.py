def NumWays(n,x,maxStep):
    if(x<0 or n<0 or n>maxStep):
        return 0
    if(x==0):
        return(n==0)
    ans=0
    for step in range(-3,4):
        ans+=NumWays(n+step,x-1,maxStep)
    return ans
    
for test in range(0,int(input())):
    n,x=map(int,input().split())
    print(int(NumWays(n,x,n)))