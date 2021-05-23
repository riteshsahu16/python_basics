#Basic building block
class phone:
	model = ""
	price = ""
	def __init__(self, model, price): #Constructor
		self.model = model
		self.price = price
		print("initialization done")

	def discounted(self,dicount_rate):
		self.price = self.price - (dicount_rate/100)*self.price

	def detail(): #static function
		print("inside detail func")


redmi = phone("Note8", 1000)
print(redmi.model, redmi.price)
redmi.discounted(10)
print(redmi.model, redmi.price)
phone.detail()

