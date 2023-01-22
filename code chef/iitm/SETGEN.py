def subs(l):
    if(len(l)==1):
        return [l]
    res=[]   
    subsets=subs(l[0:-1])
    res=res+subsets
    res.append([l[-1]])
    for sub in subsets:
        res.append(sub+[l[-1]])
    return res
    
n=int(input())
array=[]
while(n>0):
    x=int(input())
    for i in range(1,x+1):
        array.append(i)
    for i in range(len(subs(array))):
        result=",".join(str(array) for array in subs (array)[i])
        print (result.replace(","," "))
    print()
    n=n-1
    array=[]