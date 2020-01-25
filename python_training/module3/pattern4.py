for i in range(0,5):
	for j in range(5,i,-1):	
		print(" ",end="")
	print("*",end=" ")
	for k in range(1,i,1):
		print(" ",end="")
	for l in range(1,i,1):
		print(" ",end="")
	if i!=0:
		print("*",end=" ")
	print("")
print("* "*6)