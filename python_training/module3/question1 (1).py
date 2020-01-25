str=input("enter the string:")
for ch in range(0,len(str)):
	if ch.islower():
		ch=lw[i]
	else:
		ch=up[i]
print(lw+up)		