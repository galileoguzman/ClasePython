def factorial(x):
	#print "Factorial en una funcion"
	if x == 0:
		return 1
	else:
		return x * factorial(x - 1)


print factorial(3)
