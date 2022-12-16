#初始函式 __init__
#class 中函式都稱為method 方法

class phone:
	def __init__(self,number,price,waterproof,power):
		self.number=number
		self.waterproof=waterproof
		self.price=price
		self.power=power

	def play(self,num):
		self.power -= num
		if self.power < 0:
			self.power = 0



phone1 = Phone(123456789,True,8000,90)    #phone1(根據類別創建的東西就是物件)
print(phone1.power)
phone1.play(10)
print(phone1.power)