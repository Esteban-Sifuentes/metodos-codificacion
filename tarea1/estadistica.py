from sys import argv
from random import random

debug = False # activar para poder ver todos los "print"

def generaDatos(argv):
	try:
		probabilidadCero = float(argv[1])
	except:
		probabilidadCero = float(raw_input("Probalidad de ceros: "))
	try: 
		probabilidadUno = float(argv[2])
	except:
		probabilidadUno = float(raw_input("Probalidad de unos: "))
	try:
		repeticiones = int(argv[3])
	except:
		repeticiones = int(raw_input("Repeticiones por palabra: "))

	
	return (probabilidadCero, probabilidadUno, repeticiones)

def leerArchivo(nombreArchivo):
	archivo = open(nombreArchivo, "r")
	contenido = list()
	#leemos el archivo 
	for linea in archivo.readlines():
		linea = linea.split()
		contenido.append(linea)
	archivo.close()

	return contenido

def transmisor(palabra, probaCeros, probaUnos):
	palabraFinal = list()
	for lista1 in palabra:
		for elemento in lista1:
			letra = ""
			for caracter in elemento:
				if caracter == "1":
					if random() >= probaUnos: # significa que recibe una un cero
						letra += "0" # mal
					else:
						letra += "1" # bien
				else: # recibe un cero
					if random() >= probaCeros:
						letra += "1" # mal
					else:
						letra += "0" # bien
		palabraFinal.append(letra)

	# comparacion de cadenas
	for caracter in palabra:
		if palabraFinal == caracter:
			if debug: print "-", palabraFinal
			return True
		else:
			if debug: print "-", palabraFinal
			return False


############ CARACTERISTICAS DEL ARCHIVO ################
#argv[1] => (float) probabilidad de ceros               # 
#argv[2] => (float) probabilidad de unos                # 
#argv[3] => (int) repeticiones                          #
#########################################################

def main():
	#######  ARCHIVOS ####################################
	palabrasBinarias = "PALABRAS_BINARIAS.dat"           #
	######################################################

	(probaCeros, probaUnos, repeticiones) = generaDatos(argv) # genereamos los datos de necesarios para el prog
	contenido = leerArchivo(palabrasBinarias) #  leemos los archivos


	if debug: print "original: ", contenido[0]
	# el "corazon" del programa
	
	cont = 0
	for i in range(repeticiones): # repeticiones por palabra
		resultado = transmisor(contenido, probaCeros, probaUnos)
		if resultado:
			cont += 1 # sacamos las veces que fueron correcta

	probabilidad = float(cont) / float(repeticiones)
	print probabilidad


	return	

main()