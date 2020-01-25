name=input("enter the name")
la=[[0,1,0],[1,1,1],[1,0,1]]

ld=[[1,1,1],[1,0,1],[1,1,1]]

li=[[1,1,1],[0,1,0],[1,1,1]]

lt=[[1,1,1],[0,1,0],[0,1,0]]

for x in range(0,len(name))
	for i in range(0,3):
		for j in range(0,3):
			if name=="a":
				print(la[i][j])
			if name=="d":
				print(ld[i][j])
			if name=="i":
				print(li[i][j])
			if name=="t":
				print(lt[i][j])	