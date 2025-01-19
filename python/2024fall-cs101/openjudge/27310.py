n = input()
dices = []

def dfs(choses,m):


for _ in range(4):
    dices.append(input())
for _ in range(n):
    word = input()
    choses = {}
    for j in range(len(word)):
        w = word[j]
        s = []
        for i in range(4):
            if w in dices[i]:
                s.append(i)
        choses[j] = s


