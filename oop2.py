#Constructor Overloading
class phone:
	model = ""
	price = ""
	def __init__(self): #Constructor
		self.model = "default"
		self.price = 0
		print("initialization done")

	def __init__(self, model, price): #Constructor
		self.model = model
		self.price = price
		print("initialization done")


#instantiating Object
redmi = phone("Note8", 1500)
samsung = phone("M31s", 2000)

#array of objects
mobiles = [redmi, samsung]

for i in mobiles:
	print(i.model)

redmi.new = "new property"
print(redmi.new)