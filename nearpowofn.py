a=int(input())
i=1
while i<=a:
    j=2**i
    if j>a:
        print(j)
        break
    i=i+1
