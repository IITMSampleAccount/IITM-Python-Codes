for _ in range(int(input())):
    a,b=map(int, input().split())
    if (a%b==0):
        print(a//b)
    elif(a%b!=0):
        print((a%b)+(a//b))
    elif(b>a):
        print(b)