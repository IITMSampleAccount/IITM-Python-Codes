# cook your dish here
for _ in range(int(input())):
    inp = input().split()
    inp[0],inp[1]= int(inp[0]),int(inp[1])
    if inp[0]<inp[1]:print('<')     
    elif inp[0]>inp[1]: print('>')     
    else:print('=')