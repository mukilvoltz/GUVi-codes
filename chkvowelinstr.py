a=str(input())
vow=["a","i","e","o","u"]
let=list(a)
c=0
for i in let:
    if i in vow:
        print("yes")
        c=1
        break
if c == 0:
    print("no")
