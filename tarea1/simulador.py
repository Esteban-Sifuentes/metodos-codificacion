from random import random
from sys import argv

# para hacesar a atributos dentro de los metodos de la clase usar la palabra self antes

class Simulador:
	def __init__(self, density, *proba):
		self.density = density
		self.probaZero = proba[0]
		self.probaOne = proba[1]	

	def generateWords(self, longWord): 
		originalString = ""
		for cont in xrange(longWord):
			originalString += ("1", "0")[random() <= self.density] # ternary operator in python
		return originalString

	def tranMsg(self, originalString): #[1]String
		finalString = ""
		for character in originalString:
			if character == "1": # get ONE
				if random() >= self.probaOne:
					finalString += "0" # bad
				else:
					finalString += "1" # good
			else: # get ZERO
				if random() >= self.probaZero:
					finalString += "1" # bad
				else:
					finalString += "0" # good
		return finalString

	def comparator(self, originalString, finalString):
		if finalString == originalString:
			return True
		else:
			return False

####################################################
#argv[1] = (int) = long word                       #
#argv[2] = (float) = densinity of zeros in the word#  
#argv[3] = (float) = probability ones              #
#argv[4] = (float) = probability zeros             #
#argv[5] = (int) = repetitions                     #
####################################################
def main():
	sim = Simulador(float(argv[2]), float(argv[3]), float(argv[4]))
	originalString = sim.generateWords(int(argv[1]))

	success = 0
	for times in xrange(int(argv[5])):
		finalString = sim.tranMsg(originalString)
		result = sim.comparator(originalString, finalString)
		if result:
			success += 1 # equals

	probability = probability = float(success) / float(argv[5])
	print probability
	return

main()
