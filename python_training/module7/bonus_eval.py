class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
	
    def __repr__(self):
        return "%s,%s,%s"%(self.name,self.phone,self.email)
	
person1=Contact('aditi','94345','aditi@gmail.com')
person2=Contact('prachi','3654776','prachi@gmail.com')
	
dic={1:person1,2:person2}

def lookup():
    ch=int(input("enter the employee id"))
    for che in dic.keys():
        if che==ch:
            print(dic[ch])

def delete():
    ch=int(input("enter the employee id"))
        for che in dic.keys():
            if che==ch:
                del dic[ch]
                    print(dic)

def change():
    ch=int(input("enter the employee id"))
    for che in dic.keys():
        if che==ch:
            name=input("enter new name")
            no=input("enter new contact no.")
            email=input("enter new email")
            dic[ch]=name
            dic[ch]=no
            dic[ch]=email
    print(dic)             

choice=int(input("enter your choice\n1.look up\n2.add\3change\n4.delete\nQuit")) 
if choice==1:
    lookup()	
#elif choice==2:
#elif choice==3:
    change()
elif choice==4:
    delete()
#else:
    break


	
