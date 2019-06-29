from itertools import permutations
a,b=input().split()
a=str(a)
b=str(b)
d=list(a)
comb=[]
c=0
for i in permutations(a,len(a)):
    n=''.join(i)
    comb.append(n)
mi=min(comb)
l=len(comb)
for i in range(0,l):
    if mi>b:
        print(mi)
        c=1
        break
    comb.remove(mi)
    mi=min(comb)
if c == 0:
    print("-1")
