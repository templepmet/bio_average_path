crossStationList = [['', '']]

def AddSingleLine(network, stationSymbol, startNum, finishNum):
	pass

def ConstructOsakametroAdjancyList():
	network = {}
	AddSingleLine(network, 'M', 11, 30)
	AddSingleLine(network, 'P', 9, 18)
	AddSingleLine(network, 'T', 11, 36)
	AddSingleLine(network, 'Y', 11, 21)
	AddSingleLine(network, 'C', 10, 23)
	AddSingleLine(network, 'S', 11, 24)
	AddSingleLine(network, 'N', 11, 27)
	AddSingleLine(network, 'K', 11, 20)
	AddSingleLine(network, 'I', 11, 21)

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