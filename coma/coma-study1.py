import sys

mountain = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(mountain)]

result = []
result.append(data[0][0])

t = 0

for i in range(1, mountain):
    for j in range(t, 500):
        if data[i][j] > data[i][j+1]:
            result.append(data[i][j])
            t = j
            break
        elif data[i][j+1] > data[i][j]:
            result.append(data[i][j+1])
            t = j+1
            i = 1
            break
        elif data[i][j+2] > data[i][j]:
            result.append(data[i][j+2])
            t = j+2
            break
        
print(sum(result))