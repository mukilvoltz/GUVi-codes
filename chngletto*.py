a=str(input())
b=list(a)
n=len(a)
s=""
if n % 2 == 0:
    b[int(n/2)]="*"
    b[int((n/2)-1)]="*"
else:
    b[int(n/2)]="*"
s=s.join(b)
print(s)
