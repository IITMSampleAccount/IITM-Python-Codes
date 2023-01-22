# cook your dish here
TestCases = int(input())

for _ in range(TestCases):
    A, B = [int(x) for x in input().split()]
    
    #conditions
    if A>0 and B>0: 
        print('Solution')
    elif B == 0: 
        print('Solid')
    elif A==0: 
        print('Liquid')
