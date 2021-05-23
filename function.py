#scope


x = ""
print(x)
print()
def f():
	global x
	x = "change"

f()
print(x)