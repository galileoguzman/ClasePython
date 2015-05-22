for i in range(9):
	print i


diccionario = { 'a': 123, 'b': 'hola', 'c': 45.5}

print diccionario['b']

for elemento in diccionario:
	print elemento


for key, value in diccionario.items():
	print "Llave : {key}  tiene el valor {value}".format(key=key,value=value)


if diccionario.has_key('f'):
	print "Si existe la Llave A"
else:
	print "No existe"