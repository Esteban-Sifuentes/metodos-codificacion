import random, sys

debug = True

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
		intentosTotales  = 0

		for indice, caracter in enumerate(self.texto):
			intentosTotales += 1
			letraFormada = list()
			cont = 0
			if caracter == self.patron[cont]:
				sigIndice = indice
				while cont < self.lenPatron:
					try:
						letraFormada.append(self.texto[sigIndice])
					except:
						break # no hay mas caracteres que comparar
					sigIndice += 1
					cont += 1
				letraFormada = "".join(letraFormada)
				if self.patron == letraFormada:
					indiceInicalPalabraEncontrada.append(indice)
		return(indiceInicalPalabraEncontrada ,intentosTotales)

	def morrisPratt(self):
		indiceInicalPalabraEncontrada = list()
		intentos  = 0

		for indice, caracter in enumerate(self.texto):
			intentos += 1
			letraFormada = list()
			cont = 0
			if caracter == self.patron[cont]:
				sigIndice = indice
				while cont < self.lenPatron:
					try:
						letraFormada.append(self.texto[sigIndice])
					except:
						break
					sigIndice += 1
					cont += 1
				letraFormada = "".join(letraFormada)
				if self.patron == letraFormada:
					indiceInicalPalabraEncontrada.append(indice)

		return(indiceInicalPalabraEncontrada ,intentos)

	def boyerMoore(self):
		indiceInicalPalabraEncontrada = list()
		indice = 0
		intentosTotales = 0
		while indice < self.lenTexto:
			if debug: print "indice Actual", indice, " letra ", self.texto[indice]
			salto = 0
			intentosTotales += 1
			incremeto = False ###############
			try:
				valorTextoFinal = self.texto[indice + (self.lenPatron - 1)]
				valorPatronFinal = self.patron[self.lenPatron - 1]
			except:
				break
			if valorTextoFinal == valorPatronFinal:
				# significa que el ultimo elemento del patron es igual al indice del texto
				# el siguiente paso es comparar de izq-der hasta patron - 1 
				# y contar las veces que hubo comparaciones(para hacer ese salto) en caso
				# de MATCH hacer un salto del indice[0] del texto
				salto += 1
				sig = 0 # para mover de izq-der
				indiceRaiz = next = indice # next, para no alterar el indice actual
				incremeto = True
				while self.texto[next] == self.patron[sig]:
					salto += 1 # los errores tambien cuentan como salto
					next += 1 # movemos a la derecha el indice del texto
					sig += 1 # movemos a la derecha el indice del patron
					incremeto = True
					if sig == self.lenPatron - 1:
						#fue un match, hacer un salto de indiceRaiz
						indiceInicalPalabraEncontrada.append(indiceRaiz)
						indice += self.tablaSaltos[self.texto[indiceRaiz]]
						incremeto = False
						break # rompemos para seguir con el siguiente indice
			if incremeto:
				# si fueron diferentes, hacer un salto
				salto += 1
				indice += salto
			
			else:
				# no es igual, tenemos que hacer un salto
				try:
					indice += self.tablaSaltos[self.texto[indice + (self.lenPatron - 1)]]
				except:
					break
		return(indiceInicalPalabraEncontrada, intentosTotales)

def tabla(patron):
	# buscamos todas la distintas palabras en el patron y agregamos su indice

	print "patron", patron
	raw_input()


	tablaSaltos = {}
	for i in patron: 
		if not tablaSaltos.has_key(i):
			# agregamos la letra con su indice en la tabla
			tablaSaltos[i] = patron.index(i) + 1

	print tablaSaltos
	raw_input()

	return tablaSaltos

def reversa(cadena):
	# este for sirve para poner los datos de "reversa"
	for indice in range(len(cadena) - 2, -1, -1):
		yield cadena[indice]

def diferencias(texto, patron):
	patron = list(patron)
	for i in texto:
		if i not in patron:
			patron.insert(0, i)
	patron = "".join(patron)
	return patron

def main(lenTexto, lenPatron):
	gene = Generador(lenTexto, lenPatron)
	texto = gene.generarTexto()
	patron = copyPatron = gene.genererPatron()

	texto = "gatoratongataratongato"
	patron = copyPatron = "gato"

	#texto = "GCATCGCAGAGAGTATACAGTACG"
	#patron = copyPatron = "GCAGAGAG"

	#texto = "afbgggafbdbhhabbedbhhhhcfhdhaehefdecafeehbedbhbfab"
	#patron = copyPatron = "gga"

	#texto = "hccggfffaeb"
	#patron = copyPatron = "gff"

	#texto = "fheehageedagcha"
	#patron = copyPatron = "agee"

	#texto = "pfbbaabddffcfdgbgdabegdhcdcddbehhdaggabadaaegbhebgabdeaefabadgggfgafchcbfaagbcagecagefaaddchfgecacecbcheabgeadghddcabdehgbfdfghddhbebhffhaahbgcdgaeccebggdfcfhgfaebcdcehhaeffhfcbagcaghcahhbdhcgbhbdefafeghcagfefbhgfeefaahfhfhcbbhchffh"
	#patron = copyPatron = "fhfh"
	
	copyPatron = diferencias(texto, copyPatron)
	# lista temporal para guardar las letra en reversa
	copyPatron = [letra for letra in reversa(copyPatron)]
	copyPatron = "".join(copyPatron) #convertimos la lista en cadena
	
	tablaSaltos = tabla(copyPatron)

	print "tabla", tablaSaltos
	print "texto ", texto
	print "patron", patron

	comp = Comparador(texto, patron, tablaSaltos)
	(basico, intentosBasico) = comp.comparadorBasico()
	(morris, intentosMorris) = comp.morrisPratt()
	(boyer, intentosBoyer) = comp.boyerMoore()

	print "indice para basico => ", basico, " intentos ", intentosBasico
	print "indice para morris => ", morris, " intentos ", intentosMorris
	print "indice para boyer => ", boyer, " intentos ", intentosBoyer

#argv[1] = cantidad de letras para el texto rndom
#argv[2] = cantidad de letras para el patron random
main(int(sys.argv[1]), int(sys.argv[2]))