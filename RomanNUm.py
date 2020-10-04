a=str(input())
rn=["I","V","X","L","C"]
c=0
su=0
for x in a:
    if x not in rn:
        c=1
        print("-1")
        break
if c==0:
    s=len(a)-1
    for i in range(0, len(a)):
        if  a.index(a[i])!=s):
            if (a[i]=="I" and a[i+1]=="V" or a[i+1]=="X"):
                if (a[i+1]=="V"):
                    su=su+i
                    i=i+1
                if (a[i+1]=="X"):
                    su=su+9
                    i=i+1
        else:
            if(a[i]=="I"):
                su=su+1
            if(a[i]=="V"):
                su=su+5
            if(a[i]=="X"):
                su=su+10
print(su)
