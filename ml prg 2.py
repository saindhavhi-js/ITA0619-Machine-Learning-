import csv
data = list(csv.reader(open("trainingdata.csv")))[1:]
S = ['0'] * 6
G = [['?'] * 6]
for row in data:
    x, y = row[:-1], row[-1]

    if y == 'Yes':
        for i in range(6):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'
    else:
        for i in range(6):
            if S[i] != '?':
                G.append(G[0][:i] + [S[i]] + G[0][i+1:])
print("Specific:", S)
print("General:", G)
