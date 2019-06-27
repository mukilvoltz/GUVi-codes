a=int(input())
c=0
while(a%2==0):
    print(int(a/2))
    a=int(a/2)
    c=1
if c == 0:
    print(a)
