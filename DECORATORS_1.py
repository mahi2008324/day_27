def M(a):
	def inner(m):	
		if m%2==0:
			print("the given number is even")
		else:
			a(m)
	return inner
@M
def m1(m):
	print("the given number is odd ")
m1(4)
m1(3)
	