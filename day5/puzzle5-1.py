f=open ('input5-1.txt','r')
input=f.readlines()
f.close
text=[int(phrase.replace('\t'," ").replace('\n',"")) for phrase in input ]
i=0
hop=0
count=0

while True:

	if i>len(text)-1:
		break
		
	hop=text[i]
	text[i]+=1
	i=i+hop
	count+=1

print (count)
