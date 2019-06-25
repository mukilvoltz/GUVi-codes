a=int(input())
po=0
c=0
for i in range (0,a):
    po=2**i
    if po == a:
        print("yes")
        c=1
        break
if c == 0:
    print("no")
