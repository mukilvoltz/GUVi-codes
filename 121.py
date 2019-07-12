a=(input())
i=1
try:
    a=int(a)
    while(i<=a):
        arr=[]
        for j in range(1,i+1):
            arr.append(j)
        print()
        for x in arr:
            print(x,end="")
        if i!=1:
            print("1",end="")
        i=i+1
    n=int(len(arr)-1) 
    print()
    k=2
    while(k<=a):
        for x in range(0,n):
            print(arr[x],end="")
        if k<a:
            print("1",end="")
        print()
        n=int(len(arr)-k)
        k=k+1
except:
    print("Enter valid i/p")
