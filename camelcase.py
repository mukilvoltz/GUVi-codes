sentence=[str(x) for x in input().split()]
temp=""
for i in range(0,len(sentence)):
	temp+=sentence[i][0].capitalize()
	for j in range(1,len(sentence[i])):
		temp+=sentence[i][j]
	print(temp,end="")
	temp=""
