f=open ('input5-1.txt','r')
input=f.readlines()
f.close
text=[int(phrase.replace('\t'," ").replace('\n',"")) for phrase in input ]
i, hop, count = 0, 0, 0

while True:
	
	i=i+hop
	if i>=len(text):
		break
	count+=1
	hop=text[i]
	if text[i]>=3:
		text[i]-=1
	else:
		text[i]+=1
	
print (count)
