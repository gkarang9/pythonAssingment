array=[1,3,5,3,6]
sum=4
s=set()
for i in range(0,5):
	temp=sum-arr[i]
	if (temp in s):
		print ("pair with given sum "+str(sum)+"is("+str(arr[i])+","+str(temp+")")
	s.add(arr[i])		