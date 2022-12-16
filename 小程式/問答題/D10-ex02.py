#初始函式 __init__

class phone:
	def __init__(self,number,price,waterproof):
		self.number=number
		self.waterproof=waterproof
		self.price=price




phone1 = Phone(123456789,True,8000)    #phone1(根據類別創建的東西就是物件)
#phone1.number ='123456789'
#phone1.waterproof = True
#phone1.price = 8000
print(phone1.number)
print(phone1.waterproof)
print(phone1.price)