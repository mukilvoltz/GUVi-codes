n=int(input())
c=0
for i in range(0,n):
    for j in range(n-1,i,-1):
        print(" ",end="")
    for k in range(i+1,n*2):
        if k%2!=0 and c!=k and c<k:
            for l in range(0,k):
                print("*",end="")
            c=k
            break
    print("\n",end="")
d=c-2
for p in range(n-1,0,-1):
    for q in range(p,n):
        print(" ",end="")
    for s in range(0,d):
        print("*",end="")
    d-=2
    print("\n",end="")
