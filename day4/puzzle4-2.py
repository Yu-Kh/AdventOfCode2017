f=open ('input4-2.txt','r')
input=f.readlines()
f.close

text=[phrase.replace('\t'," ").replace('\n',"").split() for phrase in input ]

negphrase=0
for phrase in text:
	diction={}
	rez=0
	phrase = [sorted(letter) for letter in phrase]

	sortphrase=[]
	for word in phrase:
		tempstr=''
		for letter in word:
			tempstr+=letter
		word=tempstr
		sortphrase.append(word)
	
	for key in sortphrase:
		count = diction.get(key,0)
		diction[key] = count+1
		for key,val in diction.items():
			if val!=1: rez=1
	negphrase+=rez
passphrase = (len(text))-negphrase
print(passphrase)
