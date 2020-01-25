class Contact:
	def __init__(self,name,phone,email):
		self.name=name
		self.phone=phone
		self.email=email

		
	def set_name(self,name):
		self.name=name
		
	def get_name(self):
		return self.name
	
	def set_phone(self,phone):
		self.phone=phone
	
	def get_phone(self):
		return self.phone
		
	def set_email(self,email):
		self.email=email
		
	def get_email(self):
		return self.email
		
	def __str__(self):
		return self.name
		return self.phone
		return self.email
		
name=input("enter your name : ")
phoneno=input("enter your phoneno : ")
email=input("enter the email : ")
person=Contact(name,phoneno,email)	
print('Name:',person.get_name(),'\nPhone no:',person.get_phone(),'\nemail',person.get_email())