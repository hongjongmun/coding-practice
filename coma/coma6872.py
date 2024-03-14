# 6872 수계단
import sys

N = int(sys.stdin.readline().rstrip())

result = round(N*(N+1)/2)
# print(result)

n_box = []
for i in range(1, result+1):
    n_box.append(i)

count = 0
for i in range(N):
    for j in range(N):
        if j <= i:
            print(n_box[0], end=' ')
            n_box.remove(n_box[0])
    print()