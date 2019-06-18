b=int(input())
ary = [int(x) for x in input().split()]
ary.sort()
for i in ary:
    print(i, end = " ")
