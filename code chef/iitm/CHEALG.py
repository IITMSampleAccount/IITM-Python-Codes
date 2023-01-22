for _ in range(int(input())):
    s = input()
    a=''
    a+=s[0]
    c = 1
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            c+=1
        else:
            a+=str(c)+s[i]
            c = 1
    a+=str(c)
    
  
    print('YES' if len(a)<len(s) else 'NO')