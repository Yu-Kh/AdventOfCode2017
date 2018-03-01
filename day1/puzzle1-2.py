f=open ('input1-2.txt','r')
input=f.read()
f.close
sum=0
half = len(input)/2
for i in range (int(len(input)/2)):
	if input[i]==input[i+int(half)]:
		sum+=(int(input[i])*2)
print(sum)
