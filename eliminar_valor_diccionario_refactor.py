def imprimirDiccionario(dicc):
	for key, value in diccionario.items():
		print "Llave : {key}  tiene el valor {value}".format(key=key,value=value)


diccionario = {'a':1,'b':'hola gerardito', 'z':67.9, 'm': 5}

imprimirDiccionario(diccionario)

buscar = raw_input("Valor que desea eliminar -> ")

if diccionario.has_key(buscar):
	del diccionario[buscar]
	imprimirDiccionario(diccionario)
else:
	print "no existe"