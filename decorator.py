#Decorator : Adjective
def g(func):
	func()
	print("inside G")

@g
def f():
	print("inside f")

