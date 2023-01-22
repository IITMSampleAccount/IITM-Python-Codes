for _ in range(int(input())):
    a,b=map(int,input().split())
    x=a*2
    y=b*5
    if x>y:
        print("Chocolate")
    elif x<y:
        print("Candy")
    elif x==y:
        print("Either")