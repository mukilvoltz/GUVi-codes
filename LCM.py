a,b=input().split()
a=int(a)
b=int(b)
afact=[]
bfact=[]
comm=[]
for i in range (1,a+1):
    if a % i == 0:
        afact.append(i)
for j in range (1,b+1):
    if b % j == 0:
        bfact.append(j)
for x in afact:
    if x in bfact:
        comm.append(x)
print(int((a*b)/max(comm)))
