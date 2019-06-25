pop=int(input())
lop=int(pop/2)
cop=0
for j in range (2,lop+1):
    if pop % j == 0:
        cop=1
        print("no")
        break
if cop == 0:
    print("yes")
