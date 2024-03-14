# 책상수리
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

l = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
for i in range(N):
    if l[i] > K:
        result.append(l[i])

print(min(result))


