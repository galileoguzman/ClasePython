diccionario = {'a':1,'b':'hola gerardito', 'z':67.9, 'm': 5}

for key, value in diccionario.items():
	print "Llave : {key}  tiene el valor {value}".format(key=key,value=value)


buscar = raw_input("Valor que desea eliminar -> ")

if diccionario.has_key(buscar):
	del diccionario[buscar]
	for key, value in diccionario.items():
		print "Llave : {key}  tiene el valor {value}".format(key=key,value=value)
else:
	print "no existe"