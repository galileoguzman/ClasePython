# -*- coding: utf-8 -*-

personas = {
	('galileo','guzman'),
	('cinthya', 'rojas'),
	('osvi', 'hernandez'),
	('gerardito','iraizos'),
	('jesus', 'hernandez')
}

with open("templates/personas.html") as archivo:
	plantilla = archivo.read()

html = plantilla.split("<!--block-->")
block = ''

for n in personas:
	block += html[1].format(nombre=n[0],apellido=n[1])

print html[0] + block + html[2]