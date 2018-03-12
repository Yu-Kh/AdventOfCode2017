import math
in_num = 347991
sq=round(math.sqrt(in_num))
if sq%2==0:
	lin=sq-(sq**2-in_num)-1
print(lin)
