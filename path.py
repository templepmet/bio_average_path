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
	#print(network)
	return network

def ConstructOsakametroAdjancyMatrix():
	adjancyList = ConstructOsakametroAdjancyList()
	# Technically this is a dictionary
	# Convert List to Matrix
	nodeSize = len(adjancyList)
	adjancyMatrix = [[-1]*nodeSize for i in range(nodeSize)]
	#initialize
	for i in range(nodeSize):
		adjancyMatrix[i][i] = 0
	nodeList = ConstructNodeList() # to get index from station name
	#add adjancy
	for fromNode in adjancyList:
		fromIndex = nodeList.index(fromNode)
		for toNode in adjancyList[fromNode]:
			toIndex = nodeList.index(toNode)
			adjancyMatrix[fromIndex][toIndex] = 1
	#add crossing station
	for crossingList in crossStationList:
		for i in range(len(crossingList)):
			fromIndex = nodeList.index(fromNode)
			for j in range(i+1,len(crossingList)):
				toIndex = nodeList.index(toNode)
				adjancyMatrix[fromIndex][toIndex] = 0
				adjancyMatrix[toIndex][fromIndex] = 0
	print(adjancyMatrix)
	return adjancyMatrix

def ConstructNodeList():
	# constructs 1 dimensional list of all nodes
	ret = []
	AddNode(ret, 'M', 11, 30)
	AddNode(ret, 'P', 9, 18)
	AddNode(ret, 'T', 11, 36)
	AddNode(ret, 'Y', 11, 21)
	AddNode(ret, 'C', 10, 23)
	AddNode(ret, 'S', 11, 24)
	AddNode(ret, 'N', 11, 27)
	AddNode(ret, 'K', 11, 20)
	AddNode(ret, 'I', 11, 21)
	return ret

def AddNode(list, stationSymbol, startNum, finishNum):
	# add nodes in a single line
	for i in range(startNum, finishNum+1):
		list.append(getStationName(stationSymbol, i))


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