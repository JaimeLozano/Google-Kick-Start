# H-index score is the largest integer such that the researcher has h papers
# with at least h citations each

def scoreCalculator(N):
    score = 0
    l = []
    for i in range(0, len(N)):
        candidate = i+1
        for j in range(0,len(N)):
            if N[j] >= candidate:
                l.append(N[j])
            if len(l) == candidate:
                 break
        if candidate <= len(l) and candidate > score:
            score = candidate
        l.clear()
    return score


def indexVar(N, A):
    newList = []
    Score = 0
    ScoreList = []
    for i in range(0, N):
        newList.append(A[i])
        scoreCandidate =  scoreCalculator(newList)
        ScoreList.append(scoreCandidate)
    return ScoreList


T = int(input())
A = []
for i in range(0,T):
    N = int(input())
    A = list(map(int, input().split()))
    result = indexVar(N, A)
    print("Case {}: {}".format(i+1, result))


