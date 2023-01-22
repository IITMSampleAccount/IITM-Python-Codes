for _ in range(int(input())):

    A,B,C=map(int,input().split())
    

    if ((A+B)%2)!=0 or ((B+C)%2)!=0 or ((A+C)%2)!=0:
        print("YES")
    else:    
        print("NO")