a=str(input())
lett=list(a)
for i in range (0,len(a)):
    if i%2==0:
        print(lett[i],end="")
print(" ",end="")
for i in range (0,len(a)):
    if i%2!=0:
        print(lett[i],end="")
