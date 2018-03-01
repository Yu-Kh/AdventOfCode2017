f=open ('input2-1.txt','r')
input=f.readlines()
f.close
lines=[]
rez=0
for line in input:
	lines.append(line.replace('\t'," ").replace('\n',"").split())
ints=[[int(y) for y in x] for x in lines]

for i in range (len(ints)):
	ints[i].sort(reverse=True)
	for j in range (len(ints[i])):
		for q in range (j+1, len(ints[i])):
			if ints[i][j]%ints[i][q]==0:
				rez+=ints[i][j]/ints[i][q]
print(rez)
