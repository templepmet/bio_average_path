from cmath import inf
from collections import defaultdict

from numpy import average

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

stationIdTable = {}
countId = 0
def getStationId(symbol, id):
	global countId
	name = symbol + str(id)
	# memorize
	if name in stationIdTable:
		return stationIdTable[name]
	
	findId = -1
	for i in range(len(crossStationList)):
		if name in crossStationList[i]:
			findId = i
			break
	if findId == -1: # single station
		stationIdTable[name] = countId
		countId += 1
	else: # cross station
		for crossStationName in crossStationList[findId]:
			stationIdTable[crossStationName] = countId
		countId += 1
	return stationIdTable[name]

def AddSingleLine(network, stationSymbol, startNum, finishNum):
	for i in range(startNum, finishNum):
		fromStation = getStationId(stationSymbol, i)
		toStation = getStationId(stationSymbol, i + 1)
		network[fromStation].append(toStation)
		network[toStation].append(fromStation)
	
def ConstructOsakametroAdjacencyList():
	adjacencyList = defaultdict(lambda: [])
	AddSingleLine(adjacencyList, 'M', 11, 30)
	AddSingleLine(adjacencyList, 'P', 9, 18)
	AddSingleLine(adjacencyList, 'T', 11, 36)
	AddSingleLine(adjacencyList, 'Y', 11, 21)
	AddSingleLine(adjacencyList, 'C', 10, 23)
	AddSingleLine(adjacencyList, 'S', 11, 24)
	AddSingleLine(adjacencyList, 'N', 11, 27)
	AddSingleLine(adjacencyList, 'K', 11, 20)
	AddSingleLine(adjacencyList, 'I', 11, 21)
	return adjacencyList

def ConvertAdjacencyListToMatrix(adjacencyList):
	nodeSize = len(adjacencyList)
	adjacencyMatrix = [[inf]*nodeSize for i in range(nodeSize)]
	for i in range(nodeSize):
		adjacencyMatrix[i][i] = 0
	for fromNode in adjacencyList:
		for toNode in adjacencyList[fromNode]:
			adjacencyMatrix[fromNode][toNode] = 1
			adjacencyMatrix[toNode][fromNode] = 1
	return adjacencyMatrix

def OutputAdjacencyList(adjacencyList):
	nodeSize = len(adjacencyList)
	edges = []
	for fromNode in adjacencyList:
		for toNode in adjacencyList[fromNode]:
			edges.append((fromNode, toNode))
	edgeSize = len(edges)
	with open('adjacency_list.txt', 'w') as f:
		f.write(f'{nodeSize} {edgeSize}\n')
		for edge in edges:
			f.write(f'{edge[0]} {edge[1]}\n')

def OutputAdjacencyMatrix(adjacencyMatrix):
	nodeSize = len(adjacencyMatrix)
	with open('adjacency_matrix.txt', 'w') as f:
		f.write(f'{nodeSize}\n')
		for i in range(nodeSize):
			for j in range(nodeSize):
				if adjacencyMatrix[i][j] == 1:
					f.write('1 ')
				else:
					f.write('0 ')
			f.write('\n')

def FloydWarshall(mat):
	# calc All Shortest Path Length by Floyd-Warshall Algorithm O(n^3)
	nodeSize = len(mat)
	for k in range(nodeSize):
		for i in range(nodeSize):
			for j in range(nodeSize):
				mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
	return mat

def CalcAveragePathLength(adjacencyMatrix):
	# calc average path Length O(n^2)
	nodeSize = len(adjacencyMatrix)
	sumLength = 0
	numPath = 0
	for i in range(nodeSize):
		for j in range(i + 1, nodeSize):
			sumLength += adjacencyMatrix[i][j]
			numPath += 1
	averagePath = sumLength / numPath
	return averagePath

def main():
	adjacencyList = ConstructOsakametroAdjacencyList()
	adjacencyMatrix = ConvertAdjacencyListToMatrix(adjacencyList)
	OutputAdjacencyList(adjacencyList)
	OutputAdjacencyMatrix(adjacencyMatrix)
	
	FloydWarshall(adjacencyMatrix)
	averagePath = CalcAveragePathLength(adjacencyMatrix)
	print('AveragePath: {}'.format(averagePath))

if __name__ == '__main__':
	main()
