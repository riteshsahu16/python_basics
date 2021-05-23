#OOPS Pillars: Encapsulation, Inheritance, Polymorphism
class processor():
	def proc_detail(self):
		print("3.6 GHz")

#Encapsulation : hiding implementation details
#getter and setter methods

#property : attribute with extra-functionality
class phone(processor):
	
	def __init__(self, model, price): #Constructor
		self.model = model
		self.price = price
		print("initialization done")

	@property
	def model(self):
		print("getting model")
		return self._model

	@model.setter
	def model(self, model):
		print("setting model")
		self._model = model

	def discounted(self,dicount_rate):
		self.price = self.price - (dicount_rate/100)*self.price

	def detail(self):
		print(self.model)
		print(self.price)
		self.proc_detail()


samsung = phone("M31s", 20000)
print(samsung)
print(samsung.model)
print(samsung._model)
print("*" * 50)
print()

#Inheritance : gain all attributes & methods of base class
redmi = phone("Note8", 1500)
redmi.detail()


#Polymorphism : overriding behaviour
class computer(processor):
	def proc_detail(self):
		print("4.6 GHz")
	def details(self):
		print("Computer details")
		self.proc_detail()

cmp = computer()
cmp.details()


