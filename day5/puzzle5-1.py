f=open ('input5.txt','r')
input=f.readlines()
f.close
text=[int(phrase.replace('\t'," ").replace('\n',"")) for phrase in input ]
print(text,' i',' hop')
i=0
hop=0
count=0

while True:

	if i>len(text)-1:
		break
		
		
	elif i!=text[i]:
		
		hop=text[i]
		text[i]+=1
		i=i+hop
		count+=1
	
	elif i==text[i]:
		
		text[i]+=1
		count+=1
		
	print (text,' ',i,' ',hop)

print (count)
