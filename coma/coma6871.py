import sys

N = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().rstrip().split()))

result = []

for i in range(N):
    count = 0
    for j in range(N):
        pay = data[i]
        if data[j] >= pay:
            count += 1
    result.append(pay*count)
    
# print(result)
print(max(result))