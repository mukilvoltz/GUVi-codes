h=str(input())
nums=["1","2","3","4","5","6","7","8","9","0"]
letts=list(h)
for x in letts:
    for i in nums:
        if x==i:
            print(x,end="")
