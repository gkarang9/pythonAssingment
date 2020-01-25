class Car:
	def __init__(self,color,mileage):
		self.color=color
		self.mileage=mileage
		#print(color,mileage)
	def __str__(self):
		return 'a{self.color}car'
		
Carrrrr=Car('red',68)		