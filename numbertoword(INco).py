def fileread():
	fh=open("hello.txt","r")
	num=str(fh.read())
	return num
def numtoword(number):
	ntowones={'1':'One','2': 'Two','3':'Three','4':'Four','5':'five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten'}
	ntowtens={'2': 'Twenty','3':'Thirty','4':'Fourty','5':'fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
	for x in number:
		
