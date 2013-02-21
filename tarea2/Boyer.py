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
		self.tablaSaltos = parametro[2]

	def boyer(self):
		indiceEncontrado = list()
		indice = 0
		intentosTotales = 0
		while indice < self.lenTexto:
			if debug: print "indice Actual", indice, " letra ", self.texto[indice]
			salto = 0
			incremeto = False ###############
			try:
				valorTextoFinal = self.texto[indice + (self.lenPatron - 1)]
				valorPatronFinal = self.patron[self.lenPatron - 1]
				intentosTotales += 1
			except:
				break # rompemos para seguir con el siguiente indice
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
						indiceEncontrado.append(indiceRaiz)
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
					break # rompemos para seguir con el siguiente indice 
		return(indiceEncontrado, intentosTotales)

def crearTablaBoyer(patron):
	# buscamos todas la distintas palabras en el patron y agregamos su indice
	tablaSaltos = {}
	for i in patron: 
		if not tablaSaltos.has_key(i):
			# agregamos la letra con su indice en la tabla
			tablaSaltos[i] = patron.index(i) + 1
	return tablaSaltos

'''
def crearTablaMorris(patron):
	longitud = len(patron)
	raiz = 2 # posicion inicial de la lista
	acumulador = 0
	tablaOperaciones = list()
	tablaOperaciones.append(-1) # estos valores estan por default
	tablaOperaciones.append(0) # estos valores estan por default
	while raiz < longitud:
		if patron[raiz - 1] == patron[acumulador]:
			acumulador += 1 # incrementamos acumulador
			tablaOperaciones.append(acumulador) # agregamos
			raiz += 1 # movemos al nuevo indice
		else:
			if acumulador > 0:
				# asiganmos el nuevo acumulador
				acumulador = tablaOperaciones[acumulador]
			else:
				# si no se cumple la conficion agregara ceros
				# hasta cumplirla
				tablaOperaciones.append(0)
				raiz += 1
	return tablaOperaciones
'''

def aplicarReversa(cadena):
	# este for sirve para poner los datos de "reversa"
	for indice in range(len(cadena) - 2, -1, -1):
		yield cadena[indice]

def buscarDiferencias(texto, patron):
	patron = list(patron)
	for i in texto:
		if i not in patron:
			patron.insert(0, i)
	patron = "".join(patron)
	return patron


def main(lenTexto, lenPatron):

	#texto = "GCATCGCAGAGAGTATACAGTACG"
	#patron = copyPatron = "GCAGAGAG"

	gene = Generador(lenTexto, lenPatron)
	texto = gene.generarTexto()
	patron = copyPatron = gene.generarPatron()

	copyPatron = buscarDiferencias(texto, copyPatron)
	# lista temporal para guardar las letra en reversa
	copyPatron = [letra for letra in aplicarReversa(copyPatron)]
	copyPatron = "".join(copyPatron) #convertimos la lista en cadena

	tablaSaltos = crearTablaBoyer(copyPatron)

	# creamos el objeto
	by = Comparador(texto, patron, tablaSaltos)

	(indiceEncontrado, intentosTotales) = by.boyer()
	
	print intentosTotales
	

#argv[1] = longitud del texto
#argv[2] = longitud del patron
main(int(argv[1]), int(argv[2]))
