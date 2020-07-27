import os




def getInputFiles():

	inputFiles = []

	for inputFile in os.listdir('input'):

		if os.path.isfile(os.path.join('input',inputFile)):
			inputFiles.append(inputFile)

	return inputFiles


def read(inputFile):

	inputData = open(inputFile, 'r')
	lines = inputData.readlines()
	inputData.close()

	M = int(lines[0].strip('\n').split(' ')[0]) # the maximum number of pizza slices to order
	N = int(lines[0].strip('\n').split(' ')[1]) # the number of different types of pizza

	typesOfPizza = list(map(int,lines[1].strip('\n').split(' '))) # the number of slices in each type of pizza, in non-decreasing order

	return M, N, typesOfPizza


def solve(M, N, typesOfPizza):

	it = 0
	bestScore = -1
	bestNumberOfPizzasOrdered = 0
	bestTypesOfPizzaOrdered = []

	while it < N:

		numberOfPizzasOrdered = 0
		typesOfPizzaOrdered = []
		totalNumberOfSlices = 0

		for i in range(N-1-it, -1, -1):

			totalNumberOfSlices += typesOfPizza[i]

			if totalNumberOfSlices <= M:
				numberOfPizzasOrdered += 1
				typesOfPizzaOrdered.append(i)

				if bestScore < totalNumberOfSlices:
					bestScore = totalNumberOfSlices
					bestNumberOfPizzasOrdered = numberOfPizzasOrdered
					bestTypesOfPizzaOrdered = typesOfPizzaOrdered

			else:
				totalNumberOfSlices -= typesOfPizza[i]
				
		it += 1

	return bestScore, bestNumberOfPizzasOrdered, bestTypesOfPizzaOrdered


def write(inputFile, numberOfPizzasOrdered, typesOfPizzaOrdered):

	outputFile = open('output\\' + inputFile.replace('.in','.out'), 'w')

	outputFile.write(str(numberOfPizzasOrdered) + '\n')						# the number of different types of pizza to order
	outputFile.write(' '.join(list(map(str,typesOfPizzaOrdered[::-1]))))	# the types of pizza to order

	outputFile.close()





if __name__ == '__main__':
		
	inputFiles = getInputFiles()

	for inputFile in inputFiles:

		M, N, typesOfPizza = read('input\\' + inputFile)

		score, numberOfPizzasOrdered, typesOfPizzaOrdered = solve(M, N, typesOfPizza)

		write(inputFile, numberOfPizzasOrdered, typesOfPizzaOrdered)

		print(inputFile + ' ------> ' + str(score) + ' points')
