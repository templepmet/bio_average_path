from collections import defaultdict

crossStationList = [
 ['T13','I14'],
 ['T18','K11'],
 ['T21','K13'],
 ['N23','I18'],
 ['C20','I20'],
 ['S20','I21'],
 ['C19','N20'],
 ['C18','T23'],
 ['N18','T24'],
 ['S18','T25'],
 ['M23','T27'],
 ['C17','K15'],
 ['N16','K16'],
 ['S17','K17'],
 ['M22','K19'],
 ['Y13','C16','M18'],
 ['N15','M19'],
 ['Y15','S16','M20'],
 ['Y16','M21'],
 ['S14','N13'],
 ['C15','S13'],
 ['Y21','P18'],
 ['C10','P09']
]

def getStationName(symbol, id):
	return symbol + str(id)

def AddSingleLine(network, stationSymbol, startNum, finishNum):
	for i in range(startNum, finishNum):
		fromStation = getStationName(stationSymbol, i)
		toStation = getStationName(stationSymbol, i + 1)
		network[fromStation].append(toStation)
		network[toStation].append(fromStation)
	
def ConstructOsakametroAdjancyList():
	network = defaultdict(lambda: [])
	AddSingleLine(network, 'M', 11, 30)
	AddSingleLine(network, 'P', 9, 18)
	AddSingleLine(network, 'T', 11, 36)
	AddSingleLine(network, 'Y', 11, 21)
	AddSingleLine(network, 'C', 10, 23)
	AddSingleLine(network, 'S', 11, 24)
	AddSingleLine(network, 'N', 11, 27)
	AddSingleLine(network, 'K', 11, 20)
	AddSingleLine(network, 'I', 11, 21)
	print(network)

def ConstructOsakametroAdjancyMatrix():
	adjancyList = ConstructOsakametroAdjancyList()
	# Convert List to Matrix

def WarshallFloyd(adjancyMatrix):
	# calc minimum path length O(n^3)
	pass

def CalcAveragePathLength(adjancyMatrix):
	# calc average path Length O(n^2)
	return 0

def main():
	adjancyMatrix = ConstructOsakametroAdjancyMatrix()
	WarshallFloyd(adjancyMatrix)
	averagePath = CalcAveragePathLength(adjancyMatrix)
	print('AveragePath: {}'.format(averagePath))

if __name__ == '__main__':
	main()