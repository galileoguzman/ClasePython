from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class FrontController(BaseHTTPRequestHandler):

	def do_GET(self):
		url = self.path
		url = url.split('/')
		saludo = "Hola {nombre}".format(nombre=url[2])
		self.wfile.write(saludo)
		return


if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	#HTTPServer recibe dos parametros
	#Parametro Uno: datos del servidor
	#Parametro dos la clase manejadora de peticiones
	servidor = HTTPServer(('localhost', 8000), FrontController)
	print 'Se inicio un servidor en http://localhost:8000'
	#Para ejecutar el servidor
	servidor.serve_forever()