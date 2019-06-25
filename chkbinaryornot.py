a=input()
num=list(a)
c=0
for x in num:
    if x != "1" and x != "0":
        print("no")
        c=1
        break
if c == 0:
    print("yes")
