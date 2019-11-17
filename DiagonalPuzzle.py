#def movimientos(N,Ai):


T = int(input())
k = 0
for x in range(0, T):
	N = int(input())
	Ai =  []
	print()
	for z in range(0, N):
		Ai1 = list(input().split())
		Ai.append([ord(c) for c in Ai1[0]])
	print(Ai)
	print()

#	k = movimientos()
#	for i in range(0,N):
#		for j in range(0,N):
#			print(int(Ai[i,j]))

	#k = function(N,Ai)
	#print("Case #{}: {}".format(x+1, k))

