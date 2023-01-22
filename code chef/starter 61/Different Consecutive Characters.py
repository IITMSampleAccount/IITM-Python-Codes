for _ in range(int(input())):
    length = int(input())
    string = input()

    flag = True
    count = 0
    

    for x in range(length):
     if x+1<length:    
        if string[x] == string[x+1]:
            count += 1
    print(count)            
          
    