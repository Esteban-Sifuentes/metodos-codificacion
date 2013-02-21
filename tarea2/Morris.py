import random
from sys import argv

debug = False

# clase que genera texto y patrones
class Generador:
	def __init__(self, *longitud):
		self.texto = longitud[0]
		self.patron = longitud[1]

	def generarTexto(self):
		textoFormado = [chr(random.randrange(97, 101)) for i in xrange(self.texto)]
		textoFormado = "".join(textoFormado)
		return textoFormado

	def generarPatron(self):
		patronFormado = [chr(random.randrange(97, 101)) for i in xrange(self.patron)]
		patronFormado = "".join(patronFormado)
		return patronFormado

class Comparador:
	def __init__(self, *parametro):
		self.texto = parametro[0]
		self.patron = parametro[1]
		self.lenTexto = len(parametro[0])
		self.lenPatron = len(parametro[1])	

	def morris(self):
		indiceEncontrado= list()

		caracter = 0 # para recorrer el largo del texto
		intentos = 0 # intentos para encontrar el patron en el texto

		while caracter < self.lenTexto:
			indicePalabra = caracter
			sig = 0 # para recorrer el patron
			intentos += 1
			while sig < self.lenPatron: # recorremos el patron
				try:
					if self.texto[caracter] == self.patron[sig]:
						sig += 1 # incrementamos caracter del patron
						caracter += 1 # incrementamos caracter del texto
						iguales = True
					else: # no son iguales
						caracter += 1 # incrementamos caracter del texto
						iguales = False
						break # saltamos al sig. caracter
				except:
					iguales = False
					break # no hay mas caracteres que comparar
			if iguales:
				indiceEncontrado.append(indicePalabra) 

		return(indiceEncontrado, intentos)

def main(lenTexto, lenPatron):

	#texto = "GCATCGCAGAGAGTATACAGTACG"
	#patron = copyPatron = "GCAGAGAG"

	gene = Generador(lenTexto, lenPatron)
	texto = gene.generarPatron()
	patron = gene.generarPatron()

	# creamos el objeto
	by = Comparador(texto, patron)
	(indiceEncontrado, intentosTotales) = by.morris()
	print intentosTotales
	

#argv[1] = longitud del texto
#argv[2] = longitud del patron
main(int(argv[1]), int(argv[2]))
