datastore={"office":
            {"medical":
			[{"room-number":100,"use":"reception","sq-ft":50,"price":75},
			 {"room-number":101,"use":"waiting","sq-ft":250,"price":75},
			 {"room-number":102,"use":"examination","sq-ft":125,"price":150},
			 {"room-number":103,"use":"examination","sq-ft":125,"price":150},
			 {"room-number":104,"use":"office","sq-ft":150,"price":100}],
			"parking":
			 {"location":"premium","style":"covered","price":750}}}
def delete_room(datastore):
	roomno=int(input("enter the room no you want to delete"))
	for i in range (0,5):
		if roomno==datastore['office']['medical'][i]['room-number']:
			del datastore['office']['medical'][i]['room-number']
			del datastore['office']['medical'][i]['use']
			del datastore['office']['medical'][i]['sq-ft']
			del datastore['office']['medical'][i]['price']

def change_price(datstore):
	roomno=int(input("enter the room no"))
	pri=int(input("enter the new price"))
	for i in range (0,5):
		if roomno==datastore['office']['medical'][i]['room-number']:
			datastore['office']['medical'][i]['price']=pri

			
#delete_room(datastore)
#change_price(datastore)
#print(datastore)			

	
def add_room(datastore):
	roomno=int(input("enter the room"))
	use=input("enter the use")
	sq_ft=int(input("enter the sq-ft"))
	price=int(input("enter the price"))
	d={"room-number":roomno,"use":"use","sq-ft":sq_ft,"price":price}
	datastore['office']['medical'].append(d)


def view_room(datastore):
	roomno=int(input("enter the room no you want to view"))
	for i in range (0,15):
		if roomno==datastore['office']['medical'][i]['room-number']:
			print(datastore['office']['medical'][i]['room-number'])
			print(datastore['office']['medical'][i]['use'])
			print(datastore['office']['medical'][i]['sq-ft'])
			print(datastore['office']['medical'][i]['price'])

	
def main():
	choice=int(input("enter your choice\n 1.add\n2.delete\n3.view\n4.change price "))
	if choice==1:
		add_room(datastore)	
		print(datastore)
	if choice==2:		
		delete_room(datastore)
		print(datastore)
	if choice==3:
		view_room(datastore)
	elif choice==4:	
		change_price(datastore)
		print(datastore)	