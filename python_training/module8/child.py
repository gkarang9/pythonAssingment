from automobile import automobile
class Car(automobile):
	def __init__(self,make,model,mileage,price,door):
		automobile.__init__(self,make,model,mileage,price)	
		self.__door=door
	
	def set_door(self,door):
		self.__door=door
		
	def get_door(self):
		return self.__door

class Truck(automobile):
	def __init__(self,make,model,mileage,price,drive_type):
		automobile.__init__(self,make,model,mileage,price)
		self.__drive_type=drive_type
	
	def set_drive_type(self,drive_type):
		self.__drive_type=drive_type
		
	def get_drive_type(self):
		return self.__drive_type
		
class Suv(automobile):
	def __init__(self,make,model,mileage,price,pass_cup):
		automobile.__init__(self,make,model,mileage,price)
		self.__pass_cup=pass_cup
	
	def set_pass_cup(self,pass_cup):
		self.__pass_cup=pass_cup
		
	def get_pass_cup(self):
		return self.__pass_cup		

car=Car('2014','2010','25','100000','4')
print(car.get_make(),car.get_model(),car.get_mileage(),car.get_price(),car.get_door())		
truck=Truck('2010','2008','20','50000','2')
print(truck.get_make(),truck.get_model(),truck.get_mileage(),truck.get_price(),truck.get_drive_type())
suv=Suv('2011','2010','30','110000','5')
print(suv.get_make(),suv.get_model(),suv.get_mileage(),suv.get_price(),suv.get_pass_cup())

		
				