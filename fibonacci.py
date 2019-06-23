num=int(input())
a=0
b=1
c=1
for i in range (0,num):
    print(c, end=" ")
    c=a+b
    a=b
    b=c
