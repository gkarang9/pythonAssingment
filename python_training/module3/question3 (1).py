str=input("enter the string")
splitstr=str.split(",")
total=0
l=[int(x) for x in splitstr[1:] ]

for x in l[0:5]: 
    total = total + x
for x in l[5:]: 
    sum = sum + x
agg=(total+sum)/590*100 	
print("Robert obtained "+total+" marks out of 500 and"+sum+" marks out of 90 in practice ans successfully passed  the exam with"+agg+"% in aggregate.many congratulations to robert")