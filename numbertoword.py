def fileread():
	fh=open("hello.txt","r")
	num=str(fh.read())
	return num
def numtoword(number):
	ntowones={'1':'One','2': 'Two','3':'Three','4':'Four','5':'five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten'}
	ntowtens={'2': 'Twenty','3':'Thirty','4':'Fourty','5':'fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
	ntowten={'1':'eleven','2': 'Twelve','3':'Thirteen','4':'Fourteen','5':'fifteen','6':'Sixteen','7':'Seventeen','8':'Eighteen','9':'Nineeten'}
	words=[]
	if len(number)==3:
		words.append(ntowones[number[0]])
		words.append('hundred')
		words.append('and')
		if number[1]!="1":
			words.append(ntowtens[number[1]])
			if number[2]!="0":
			    words.append(ntowones[number[2]])
		else:
		    if number[2]!="0":
			    words.append(ntowten[number[2]])
	if len(number)==2:
		if number[0]!="1":
			words.append(ntowtens[number[0]])
			if number[1]!="0":
			    words.append(ntowones[number[1]])
		else:
			words.append(ntowten[number[1]])
	if len(number)==1:
		words.append(ntowones[number[0]])
	return words
def filewrite(num2words):
	fh.write(num2words)
if __name__=='__main__':
	numb=fileread()
	n2w=numtoword(numb)
	filewrite(n2w)
