people = {1:{'name':'aditi','age':'19','sex':'Female'},2:{'name':'pratham','age':'20','sex':'Male'}}
for p_id,p_info in people.items():
	print("\nPerson ID",p_id)
	for key in p_info:
		print(key+'.',p_info[key])