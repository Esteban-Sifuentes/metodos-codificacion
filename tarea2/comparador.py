def MorrisPratt_osvaldo(texto, llave):
	longitud = len(llave)
	indiceInicalPalabraEncontrada = list()
	intentos  = 0

	for indice, caracter in enumerate(texto):
		intentos += 1
		letraFormada = list()
		cont = 0
		if caracter == llave[cont]:
			sigIndice = indice
			while cont < longitud:
				letraFormada.append(texto[sigIndice])
				sigIndice += 1
				cont += 1
			letraFormada = "".join(letraFormada)
			if llave == letraFormada:
				indiceInicalPalabraEncontrada.append(indice)
				
	return(indiceInicalPalabraEncontrada ,intentos)

def MorrisPratt_pagina(texto, llave):
	longitud = len(llave)
	indiceInicalPalabraEncontrada= list()
	
	caracter = 0 # para recorrer el largo del texto
	intentos = 0 # intentos para encontrar la llave en el texto

	while caracter < len(texto):
		indicePalabra = caracter
		sig = 0 # para recorrer la llave
		intentos += 1
		while sig < len(llave): # recorremos la llave
			if texto[caracter] == llave[sig]:
				sig += 1 # incrementamos caracter de la llave
				caracter += 1 # incrementamos caracter del texto
				iguales = True
			else: # no son iguales
				caracter += 1 # incrementamos caracter del texto
				iguales = False
				break

		if iguales:
			indiceInicalPalabraEncontrada.append(indicePalabra) 

	return(indiceInicalPalabraEncontrada, intentos)


def BoyerMoore_osvaldo(texto, llave):
	#print "largo", len(texto)
	#print "largo LLAVE", len(llave)
	indiceInicalPalabraEncontrada = list()
	caracter = 0
	intentos = 0
	while caracter < len(texto):
		intentos += 1
		if debug:
			print "caracter a probar", caracter
		indicePalabras = caracter # para nunca perder en que posicion estamos
		try:
			# texto a comparar
			pedazoTexto = [texto[caracter + i] for i in xrange(len(llave))] 
		except:
			break # no hay mas caracteres que comparar
		anterior = len(llave) - 1 # el -1 para que no salga fuera del rango
		acumulador = 0 # nos indicara cuantas pocisiones tenemos que brincar
		ultimo = len(llave) - 1 # Para no bricar el indice[0]
		if caracter == 0: # solo hacemos esto para el primer elemento porque tiene 
						  # varias restricciones		
			while anterior > -1:
				#print "anterior: ", anterior
				# comparamos el pedazo de texto contra la llave de der-izq
				pedazoTexto = "".join(pedazoTexto)
				iguales = False
				if(pedazoTexto[ultimo] != llave[ultimo]) and \
														(pedazoTexto[ultimo] == llave[0]):
					# significa que el ultimo elemento del pedazo de texto y el ultimo elemento
					# de la llave son distintos pero(and) el ultimo elemento del pedazo de texto
					# es igual al primer elemento de la llave
					#print "2"
					caracter += ultimo # restamos 1 a longitud porque cabe la 
									   # posibilidad que el ultimo elemento sea el 
									   # inicio de la llave
					break # pasemos al sig. caracter				
				elif(pedazoTexto[anterior] == llave[anterior]):
					# "igual"
					#print "3"
					acumulador += 1
					anterior -= 1
					iguales = True
				else:
					#print "4"
					# "se equivoco en la busqueda"
					acumulador += 1
					caracter += acumulador
					iguales = False
					break # pasemos al sig. caracter
			if iguales:
				#print "PRIMER ELEMENTO - IGUALES"
				indiceInicalPalabraEncontrada.append(indicePalabras)
				caracter += acumulador
		else:
			# ya estamos en el algoritmo de comparacion
			while anterior > -1: # Para no bricar el indice[0]
				if pedazoTexto[anterior] == llave[anterior]:
					acumulador += 1
					anterior -= 1
					iguales = True
				elif(pedazoTexto[0]) == llave[0]:
					# significa los primeros elementos de cada lista es igual pero el
					#ultimo es diferente, es este caso hacer un brinco del tamano de la letra
					caracter += len(llave) 
					iguales = False
					break # pasemos al sig. caracter
				else:
					# "se equivoco en la busqueda"
					acumulador += 1 
					caracter += acumulador
					iguales = False
					break # pasemos al sig. caracter
			if iguales:
				#print "IGUALES"
				indiceInicalPalabraEncontrada.append(indicePalabras)
				caracter += acumulador
	
	return(indiceInicalPalabraEncontrada, intentos)

debug = False

TEXTO = "gatoratongataratongato"
LLAVE = "gato"

print "texto: ", TEXTO
print "llave: ", LLAVE

indicePalabras, intentos = MorrisPratt_pagina(TEXTO, LLAVE)
indicePalabras2, intentos2 = MorrisPratt_osvaldo(TEXTO, LLAVE) 
indicePalabras3, intentos3 = BoyerMoore_osvaldo(TEXTO, LLAVE)

print "MorrisPratt =>  ", indicePalabras, "intentos", intentos
print "BoyerMoore =>  ", indicePalabras3, "intentos", intentos3