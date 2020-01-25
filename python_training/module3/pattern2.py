sp =5
spp =4
for i in range (0,5,2):
	for j in range(0, sp):
		print(end=" ")
	sp = sp - 1	
	for j in range(0,i+1,1):
		print("*",end="")
	print("")

for i in range (1,5,2):
	for j in range(0,spp):
		print(end=" ")
	spp = spp + 1
	for j in range(4,i,-1):
		print("*",end="")
	print("")