print "Render usuario"

with open("templates/usuario.html") as archivo:
	'''Leemos un archivo y el contenido lo guardamos en la variable plantilla como una cadena'''
	plantilla = archivo.read()

print plantilla.format(nombre="Juanito",apellidos="Zuckerberth", edad=12)