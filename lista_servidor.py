from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class FrontController(BaseHTTPRequestHandler):

	def do_GET(self):
		
		#Definir y concatenar la plantilla
		personas = {('galileo','guzman'), ('cinthya', 'rojas'), ('osvi', 'hernandez'), ('gerardito','iraizos'),('jesus', 'hernandez')}

		with open("templates/personas.html") as archivo:
			plantilla = archivo.read()

		html = plantilla.split("<!--block-->")
		block = ''

		for n in personas:
			block += html[1].format(nombre=n[0],apellido=n[1])

		salida = html[0] + block + html[2]

		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(salida)
		
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