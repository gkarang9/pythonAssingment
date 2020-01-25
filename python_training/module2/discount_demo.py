pack=int(input("enter the no. of package purchased"))
if pack<10:
    pes=0.0
elif pack<=19:
	pes=10
	
elif pack<=49:
	pes=20

elif pack<=99 :
	pes=30

else:
	pes=40

dis=pes/100*99
print("amount of discount is $",dis)
print("total amount is $",99-dis)	