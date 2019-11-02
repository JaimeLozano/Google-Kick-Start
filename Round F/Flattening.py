# Wall 
# 	- N sections --> 1 to N --> left to right
# 	- Not all sections are of the same weight --> the i-th is Ai metres tall
# 	- Rebuilding some sections --> can choose height of each sections.
# 	- happy --> if --> i (1 <= i < N) where Ai != Ai+1 is not more than K
# 	- Fewest sections os the wall blotch needs to rebuild so that he will be happy
#
# Input
# 	- First lines --> T test cases.
# 	- Second line --> N and K --> K = max number of changes in height between adjacent sections --> K = Alturas que pueden haber adjacentes
# 	- Third line --> N integers --> Ai
# Output 
# 	Case --> y = fewest sections that blotch has to rebuild 
# 	

# Ka --> actual K values

def KaCreator(N, Ai): # Creates new Ka
	Ka = 0
	for i in range(0, N-1):
	 	if Ai[i] != Ai[i+1]:
	 		Ka += 1
	return Ka


def simpleAdjacense(N, Ai, Y): # Search for [x y x] values and changes y = x
	valueChanged = False
	for i in range(1, N-1):
		if Ai[i-1] == Ai[i+1] and Ai[i] != Ai[i+1]:
			Ai[i] = Ai[i+1]
			valueChanged = True
			Y += 1
			break
	return Ai, valueChanged, Y

def doubleAdjacense(N, Ai, Y): # Search for [x y y x] values and changes first y = x
	valueChanged = False
	for i in range(1, N-2):
		if Ai[i-1] == Ai[i+2] and Ai[i] != Ai[i-1]:
			Ai[i] = Ai[i-1]
			valueChanged = True
			Y += 1
			break
	return Ai, valueChanged	, Y

def simpleChange(N, Ai, Y): # Search for [x y] values and changes y = x
	valueChanged = False
	for i in range(1, N):
		if Ai[i] != Ai[i-1]:
			Ai[i] = Ai[i-1]
			Y += 1
			break
	return Ai, Y

T = int(input())
Y = 0
for x in range(0, T):
	N, K = map(int, input().split())
	Ai = list(map(int, input().split()))
	Ka = KaCreator(N, Ai)
	while Ka>K:
		Ai, valueChanged, Y = simpleAdjacense(N, Ai, Y)
		if valueChanged == False:
			Ai, valueChanged, Y = doubleAdjacense(N, Ai, Y)
			if valueChanged == False:
				Ai, Y = simpleChange(N, Ai, Y)	
		Ka = KaCreator(N, Ai)
	print("Case #{}: {}".format(x+1, Y))
	Y = 0
  	

