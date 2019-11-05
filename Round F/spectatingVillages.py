# Kickstartia
# 	- V villages --> 1 to V --> connected by V-1 bidirectional roads
# 	- The i-th road connects village Xi to village Yi.
# 	- Each road connect two villages
# 	- No two road connect the same two villages
# 	- There is exactly one sequence of roads that connects any two villages
# 	- Some villages are more beautifull than others --> The i-th village has beauty of Bi (can be negative)
# 	- Village is illuminated if there is a lighthouse built in it or there is a village with lighthouse directly connected.
# 	- You may build as many (even zero) lighthouse.
# 	- Maximum possible sum of beauty values of illuminated villages you can obtain

# Input
# 	- First T
# 	- Second integer V
# 	- Third List of integer Vi with beauty
# 	- V-1 lines follows Xi and Yi

def maxBeautyComprober(beautyList, binaryList, V, Road):
	maxValue = 0
	for i in range(0, len(binaryList)):
		for j in range(0, len(binaryList)):
			if i == j:
				pass
			elif binaryList[i] == 1:
				maxValue = maxValue + beautyList[i]
				break
			elif [i+1,j+1] in Road or [j+1,i+1] in Road:
				if binaryList[j] == 1:
					maxValue = maxValue + beautyList[i]
					break
	return maxValue


T = int(input())
binaryList = []
MAX = 0
Road = []
for x in range(0,T):
	V = int(input())
	Vb = list(map(int, input().split()))
	for i in range(0, V-1):
		Xi, Yi = map(int, input().split())
		Road.append([Xi,Yi])
	rangeOptions = 2**V
	for i in range(0, rangeOptions):
		binaryList = list(bin(i))
		binaryList.pop(0)
		binaryList.pop(0)
		binaryList = list(map(int, binaryList))
		if len(binaryList) != V:
			put0 = V-(len(binaryList))
			for j in range(0, put0):
				binaryList.insert(0,0)
		maxCandidateNumber = maxBeautyComprober(Vb, binaryList , V, Road)
		if maxCandidateNumber > MAX:
			MAX = maxCandidateNumber
	print("Case #{}: {}".format(x+1, MAX))
	MAX = 0
	Road.clear()
	Vb.clear()
