def obtenerLetras(cadena):
	letras = dict()
	for caracter in cadena:
		if caracter in letras:
			letras[caracter] += 1
		else:
			letras[caracter] = 1
	letras = letras.items()
	return letras


def ordenarMenorMayor(letras): # lista de tuplas
	# ordena de mayor a menor por el elemento[1] de la tupla
	return sorted(letras, key=lambda o: o[1])


def main():
	cadena = "aaabbcccccddeeeefhhhhhxx"
	letras = obtenerLetras(cadena)
	print letras
	letrasOrdenadas = ordenarMenorMayor(letras)
	print letrasOrdenadas
	

	

main()