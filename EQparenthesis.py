a=str(input())
ao=0
ac=0
bo=0
bc=0
co=0
cc=0
for x in a:
    if x=="{":
        ao=ao+1
    elif x=="}":
        ac=ac+1
    elif x=="(":
        bo=bo+1
    elif x==")":
        bc=bc+1
    elif x=="[":
        co=co+1
    elif x=="]":
        cc=cc+1
if (ao==ac and bo==bc and co==cc):
    print("yes")
else:
    print("no")
