import random

# clase que genera texto y patrones
class Generador:
	def __init__(self, *longitud):
		self.texto = longitud[0]
		self.patron = longitud[1]

	def generarTexto(self):
		textoFormado = [chr(random.randrange(97, 105)) for i in xrange(self.texto)]
		textoFormado = "".join(textoFormado)
		return textoFormado

	def genererPatron(self):
		patronFormado = [chr(random.randrange(97, 105)) for i in xrange(self.patron)]
		patron = "".join(patronFormado)
		return patron


# Clase que se encarga de comparar un patron si esta dentro de un texto(strings)
class Comparador:
	def __init__(self, *parametro):
		self.texto = parametro[0]
		self.patron = parametro[1]
		self.lenTexto = len(parametro[0]) 
		self.lenPatron = len(parametro[1])
		self.tablaSaltos = parametro[2]

	def comparadorBasico(self):
		indiceInicalPalabraEncontrada = list()
		intentos  = 0

		for indice, caracter in enumerate(self.texto):
			intentos += 1
			letraFormada = list()
			cont = 0
			if caracter == self.patron[cont]:
				sigIndice = indice
				while cont < self.lenPatron:
					letraFormada.append(self.texto[sigIndice])
					sigIndice += 1
					cont += 1
				letraFormada = "".join(letraFormada)
				if self.patron == letraFormada:
					indiceInicalPalabraEncontrada.append(indice)

		return(indiceInicalPalabraEncontrada ,intentos)

	def morrisPratt(self):
		indiceInicalPalabraEncontrada= list()
		
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
				indiceInicalPalabraEncontrada.append(indicePalabra) 

		return(indiceInicalPalabraEncontrada, intentos)

	def boyerMoore(self):
		indiceInicalPalabraEncontrada = list()
		print "En proceso..."
		intentos = 0
		return(indiceInicalPalabraEncontrada, intentos)

def tabla(patron):
	# buscamos todas la distintas palabras en el patron y agregamos su indice
	tablaSaltos = {}
	for i in patron: 
		if not tablaSaltos.has_key(i):
			# agregamos la letra con su indice en la tabla
			tablaSaltos[i] = patron.index(i) + 1
	return tablaSaltos


def reversa(cadena):
	# este for esta para poner los datos de "reversa"
	for indice in range(len(cadena) - 2, -1, -1):
		yield cadena[indice]

def diferencias(texto, patron):
	patron = list(patron)
	for i in texto:
		if i not in patron:
			patron.insert(0, i)
	patron = "".join(patron)
	return patron

def main():
	#gene = Generador(4, 3)
	#texto = gene.generarTexto()
	#patron = gene.genererPatron()

	texto = "gatoratongataratongato"
	patron = copyPatron = "gato"

	#texto = "GCATCGCAGAGAGTATACAGTACG"
	#patron = copyPatron = "GCAGAGAG"

	copyPatron = diferencias(texto, copyPatron)
	# lista temporal para guardar las letra en reversa
	copyPatron = [letra for letra in reversa(copyPatron)]
	copyPatron = "".join(copyPatron) #convertimos la lista en 
	tablaSaltos = tabla(copyPatron)

	comp = Comparador(texto, patron, tablaSaltos)
	(basico, intentosBasico) = comp.comparadorBasico()
	(morris, intentosMorris) = comp.morrisPratt()

	print "indice para basico => ", basico
	print "indice para morris => ", morris 


main()