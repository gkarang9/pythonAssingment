matrix1=[]
for i in range(5):
	matrix1.append([])
	for j in range(5):
		matrix1[i].append(j)
print(matrix1)
  

matrix2=[[j for j in range(10)]for i in range(5)] 
print(matrix2) 