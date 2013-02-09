# uno que genera palabras binarias pseudoaleatoriamente usando 
# frecuencias definidas como parametros para los ceros y los unos,

from random import randrange, randint, random
from sys import argv

MIN = 3
MAX = 5

def generarDatos(argv):
	try: 
		largo = int(argv[1])
	except:
		largo = int(raw_input("largo en la palabra: "))
	try: 
		densidad = float(argv[2])
	except:
		densidad = float(raw_input("Cantidad la densidad(para generar ceros): "))
	
	return largo, densidad

def generarPalabras(largoPalabra, densidad):
	palabras = list()

	caracter = ""
	for numero in range(largoPalabra): 
		caracter += ("1","0")[random() <= densidad] # operador ternario en python
	palabras.append(caracter) # agregamos la letra a las palabras
	return palabras

def imprimirArchivo(lista, nombreArchivo):
	archivo = open(nombreArchivo, "w")
	for letra in lista:
		print >> archivo, letra
	archivo.close()
	return

############# CONFIGURACION DEL PROGRAMA ##############
## PARAMETROS DE ENTRADA                              #
#argv[1] = largo de la palabras                       #
#argv[2] = densidad para generar ceros                #
#######################################################

def main():
	
	## ARCHIVOS ###########################################
	PALABRASBINARIAS = "PALABRAS_BINARIAS.dat"            #
	#######################################################

	(largoPalabras, densidad) = generarDatos(argv) # leemos los datos necesarios para el programa
	palabras = generarPalabras(largoPalabras, densidad) # generemos palabras aleatoriamente
	imprimirArchivo(palabras, PALABRASBINARIAS) # guardamos en achivo

	#print "densidad para formar ceros:", densidad, "y densidad para unos:", 1 - densidad 

	return

main()