# cook your dish here
for i in range(int(input())):
    
    a,b=input(),input()
    print("yes" if ((a[0]=="o" or b[0]=="o") and(a[1]=="b" or b[1]=="b")and (a[2]=="b"or b[2]=="b")) or ((a[1]=="o" or b[1]=="o") and(a[2]=="b" or b[2]=="b")and (a[0]=="b"or b[0]=="b")) or ((a[2]=="o" or b[2]=="o") and(a[1]=="b" or b[1]=="b")and (a[0]=="b"or b[0]=="b")) else "no")
    