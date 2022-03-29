number=[4,13,15,70,51,23,38,9,12,5]
even=[]
odd=[]
for i in number:
	if i%2==0:
		i=even
		even.sort()
		for j in even:
			print(j)
