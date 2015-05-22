from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class FrontController(BaseHTTPRequestHandler):

	def do_GET(self):
		url = self.path

		if url == '/contacto':
			pagina = 'contacto'
		elif url == '/acerca':
			pagina = 'acerca'
		else:
			pagina = '404'

		#Debug para un developer feliz
		print "Pagina solicitada --- " + url
		#Definir y concatenar la plantilla
		with open("templates/"+pagina+".html") as archivo:
			plantilla = archivo.read()

		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(plantilla)
		
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