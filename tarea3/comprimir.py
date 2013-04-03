
def obtenerLetras(cadena):
	letras = dict()
	for caracter in cadena:
		if caracter in letras:
			letras[caracter] += 1
		else:
			letras[caracter] = 1
	letras = letras.items()
	return letras


# ordena de mayor a menor por el elemento[1] de la tupla
def ordenarMenorMayor(lista, metodo="listaTuplas"): # lista de tuplas
	if metodo == "listaTuplas":
		return sorted(lista, key=lambda o: o[1])
	else:
		return sorted(lista, key=lambda o: o[0][1])


def crearEnlaces(listaLetras): # recibe una lista de tuplas
	nodos = dict()

	while len(listaLetras) > 1:
		# tomamos los dos nodos menores a unir...
		izq = listaLetras[0]
		der = listaLetras[1]
		# los unimos...
		valorNodo = izq[1] + der[1]
		nodos[(izq[0], valorNodo)] = 0
		nodos[(der[0], valorNodo)] = 1
		# creeamos el nuevo nodo...
		listaLetras.append((valorNodo, valorNodo))
		# eliminamos los nodos procesados...
		listaLetras.pop(0)
		listaLetras.pop(0)
		# ordenamos de menor a mayor
		listaLetras = ordenarMenorMayor(listaLetras)
	nodos = nodos.items()	

	return(nodos, listaLetras[0])


def buscarRaiz(nodoActual, nodos, nodoFinal):
	raiz = list()
	
	while nodoActual != nodoFinal[0]:
		raiz.append(nodoActual[1]) # agregamos el valor de la arista
		nodoActual = nodoActual[0][1] # asignamos el nuevo nodo actual
		# buscamos la tupla del nodoActual
		for items in nodos:
			if items[0][0] == nodoActual:
				nodoActual = items
				break
	return raiz

def main():

	debug = True

	if debug:
		cadena = "aaabbcccccddeeeefhhhhxxh"
	else:
		cadena = '''Huffman code is a lookup table that's generated by a compression scheme known as 
		the Huffman algorithm. While the table itself is only a part of the complete algorithm, it's 
		probably the most challenging component to grasp. It is a binary tree that stores values based on frequency. 
		The more frequent the value, the closer to the root it is located and the smaller its binary representation. 
		Once the lookup table is created, it is used to compress the data, and subsequently to decompress it.'''
	
	# filtro para quitar tabulaciones y saltos de linea
	cadena = cadena.replace("\t", "").replace("\n", " ") 

	letras = obtenerLetras(cadena)
	# ordenar las letras unicas por frecuencias menor-mayor	
	letrasOrdenadas = ordenarMenorMayor(letras)
	# buscamos los enlaces de los nodos
	(nodos, nodoFinal) = crearEnlaces(letrasOrdenadas)
	# ordenar los nodos de menor a mayor
	nodos = ordenarMenorMayor(nodos, "nodos")

	# buscamos las raices(el valor de la arista) de cada nodo
	raices = list()
	while len(nodos) > 0:
		nodoActual = nodos[0] # tomamos el primer elemento de los nodos
		raices.append((nodoActual[0][0], buscarRaiz(nodoActual, nodos, nodoFinal))) # buscamos su raiz
		nodos.pop(0) # eliminamos el nodo procesado

	print raices
	print raices[0][1]


	for indice, tupla in enumerate(raices):
		reversa = tupla[1].reverse()
		print reversa
		raices[indice][1] = reversa 



	print "-----"
	
	print "Total de caracteres en la cadena:", len(cadena)
	print "Total de caracteres unicos:", len(letras)
	print "Raices:", raices



main()