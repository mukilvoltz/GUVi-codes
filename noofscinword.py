a=input()
letters=list(a)
asc=0
c=0
for l in letters:
    asc=ord(l)
    if asc>33 and asc<47:
        c=c+1
    elif asc>58 and asc<64:
        c=c+1
    elif asc>91 and asc<96:
        c=c+1
    elif asc>124 and asc<126:
        c=c+1
print(c)
