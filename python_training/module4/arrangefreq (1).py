list1=[]
l=int(input("enter no of elements"))
for i in range(0, l): 
    ele = int(input()) 
    list1.append(ele) 
print(list1) 
new= set(list1)
print("unique values are",new)
for i in range(0,len(list1)):
	list1.count(list1[i])