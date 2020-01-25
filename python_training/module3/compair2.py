L1=[1,3,5,6,3]
L2=[3,5,6,4]
def pairs(sum):
	sum=5
	count=0
	for i in range(0,len(L1)):
		print()
		for j in range (0.len(L2)):
			if L1[i]+L2[j]==sum:
				count=count+1
				print(L[i],L2[j])
	return count
print("count pair is ",pairs(sum))	