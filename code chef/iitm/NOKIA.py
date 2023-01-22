# cook your dish here
def min_length(k):
    if(k==0):
        return 0
    if(k==1):
       return 2
    else:
        return k+1+min_length((k-1)//2)+min_length((k-1)-(k-1)//2)
        
t=int(input())
for i in range(t):
    n,m=[int(x) for x in input().split()]
    if(m<min_length(n)):
        print(-1)
    elif(m>n*(n+3)/2):
        print(m-(n*(n+3)//2))
    else:
        print(0)