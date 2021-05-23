#override method
class phone:
	
	def __init__(self, model, price): #Constructor
		self.model = model
		self.price = price
		print("initialization done")

	def __str__(self):
		print("converting to string")
		return self.model + " " + str(self.price)

	def print_all_phones(phones):
		for phone in phones:
			print(phone)

	def __eq__(self, other):
		if self.price == other.price:
			return True
		return False

	__repr__ = __str__

galaxy = phone("galaxy J8", 20000)
#galaxy = phone("M31s", 20000)

redmi = phone("Note8", 1500)
samsung = phone("M31s", 20000)
print()

print(type(galaxy))
print(galaxy)

mobiles = [redmi, samsung, galaxy]
phone.print_all_phones(mobiles)
print()

print(galaxy == samsung)
print(id(galaxy) , id(samsung))
print("*" * 50)

print(mobiles)