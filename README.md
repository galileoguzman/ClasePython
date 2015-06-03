# clase python
## proyecto creado para explicar el funcionamiento en entornos web con Python

Python <https://www.python.org/> es uno de los lenguajes más populares hoy en día, promoviendo el desarrollo ágil de proyectos con una sintaxis limpia.

![Python logo](https://www.python.org/static/img/python-logo@2x.png "Python Logo")

Existen muchos Frameworks para desarrollo web con Python:

1. Django <https://www.djangoproject.com/>
2. Flask <http://flask.pocoo.org/>
3. WebPy <http://webpy.org/> 
4. App Engine <https://appengine.google.com/>

Por mencionar algunos.

En este proyecto se puede ver diferentes aspectos del uso de plantillas directamente desde la clase STR (String) con su metodo format:

	Uso de método format python:
	
	nombre = "Benito Juárez"
	frase = "El derecho al respecto ajeno es la paz"
	
	#ejemplo de format
	
	salida = "El Lic. {nomb} dijo {fras} ".format(nom=nombre,fras=frase)
	
	print salida
	
El código anterior es un ejemplo de como se implementan las plantillas en este proyecto.

	#Renderizar una plantilla con Python y format
	
	with open("archivo.html") as archivo:
		plantilla = archivo.read()
	
	print plantilla.format(nombre="Juanito",apellidos="Juárez", edad=52)
	
El código anterior muestra el uso de como renderizar una plantilla en python.

Python cuenta con una clase SimpleHTTPServer la cual genera un servidor de archivos en el directorio que lo ejecutemos:

	python -m SimpleHTTPServer
	
Con Python podemos manejar cualquier petición HTTP con la clase BaseHTTPServer.BaseHTTPRequestHandler Sí tienes experiencia con JAVA EE podras entender el código y saber como implementarlo manualmente.

####### Proyecto creado como explicación para el departamento de Desarrollo de Sistema de MRCI Tech
