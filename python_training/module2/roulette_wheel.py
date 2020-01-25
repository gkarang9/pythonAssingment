pocket=int(input("enter the no. of pockets"))
if pocket==0:
	color="green"
   
elif pocket<=10:
	if pocket%2==0:
		color="black"
	else:
		color="red"

elif pocket<=18:
	if pocket%2==0:
		color="red"
	else:
		color="black"

elif pocket<=28:
	if pocket%2==0:
		color="black"
	else:
		color="red"

elif pocket<=36:
	if pocket%2==0:
		color="red"
	else:
		color="black"		
else :
	color="out of range"
print("no. of pocket is:",pocket)
print("color of pocket is:",color)	
		
		
      