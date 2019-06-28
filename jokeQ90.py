a=str(input())
num=["1","2","3","4","5","6","7","8","9","0"]
lett=list(a)
for x in lett:
    for i in num:
        if x==i:
            print(x,end="")
