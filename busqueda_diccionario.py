diccionario = {'a':1,'b':'hola gerardito', 'z':67.9, 'm': 5}

buscar = raw_input("Valor de busqueda -> ")

if diccionario.has_key(buscar):
	print "Si existe el obj {busqueda} tiene el valor {value}".format(busqueda=buscar, value=diccionario[buscar])
else:
	print "no existe"