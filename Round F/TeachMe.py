def NListExtraction(N):
	NList = []
	for i in range(0, N):
		Nsi = list(map(int, input().split()))
		input.clear()
		NList.append(Nsi)
	return NList

def eachSkillComprobation(numberComprobation, List): # Comproves each number in other N
	iSize = List[0]
	repetition = False
	for i in range(1, iSize+1):
		if List[i] == numberComprobation:
			repetition = True
			break
	return repetition

def skillComprobation(NList): # Select each N list and sum Y in case repetition
	Y = 0
	for i in range(0, len(NList)):
		jSize = NList[i][0]
		repetition = False
		alreadyY = []
		for j in range(1, jSize+1):
			for k in range(0, len(NList)):
				repetition = eachSkillComprobation(NList[i][j], NList[k])
				if repetition == False and k not in alreadyY:
					Y += 1
					alreadyY.append(k)
		alreadyY.clear()

	return Y

T = int(input())
Y = 0
for x in range(0, T):
	N, S = map(int, input().split())
	NList = NListExtraction(N)
	Y = skillComprobation(NList)
	print("Case #{}: {}".format(x+1, Y))
