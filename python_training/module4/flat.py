#flatter matrix
list1=[[1,3,2],[5,4],[6,9,7,8]]
flated_list=[]
for sublist in matrix:
	for val in sublist:
		flated_list.append(val)
print(flated_list)		


flatt_matrix=[val for sublist in matrix for val in sublist]
print(flatt_matrix)
