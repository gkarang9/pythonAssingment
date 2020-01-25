value[0,0,0][0,0,0][0,0,0]
for r in range(3):
	for c in range(3):
		value[r][c]=int(input("enter the values"))
		if value[0][0]+value[0][1]+value[0][2]==value[1][0]+value[1][1]+value[1][2]==value[2][0]+value[2][1]+value[2][2]==value[0][0]+value[1][0]+value[2][0]==value[0][1]+value[1][1]+value[2][1]==value[0][2]+value[1][2]+value[2][2]==value[0][0]+value[1][1]+value[2][2]:
			print("the square is magical")
		else:
			print("the square is not magical")