import random 
class Coin:
	def __init__(self):
		self.sideup = 'Heads'
	def toss(self):
		if random.randint(0,1)==0:
			self.sideup='Head'
		else :
			self.sideup='Toss'
	def get_sideup(self):
		return self.sideup

ccc=Coin()		