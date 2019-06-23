a=input()
num=["1","2","3","4","5","6","7","8","9","0"]
letters=list(a)
c=0
for l in letters:
    for n in num:
        if l == n:
            c=c+1
print(c)
