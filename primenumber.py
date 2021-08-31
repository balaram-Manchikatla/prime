print('Enter the positive integer')
z=int(input())
if z==2:
	print('prime')
	exit()
if z==1:
	print('not prime')
	exit()
count=0
i=2
while i<=(int(z**0.5)):
	if(z%i==0):
		count=1
		break
	i=i+1
if count==1:
	print('not prime')
else:
	print('prime')
