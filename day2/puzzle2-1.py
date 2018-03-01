f=open ('input2-1.txt','r')
input=f.readlines()
f.close
lines=[]
res=0
for line in input:
	lines.append(line.replace('\t'," ").replace('\n',"").split())
int_lines=[[int(y) for y in x] for x in lines]

for i in range (len(int_lines)):
	dif = max(int_lines[i])-min(int_lines[i])
	res+=dif
print(res)
