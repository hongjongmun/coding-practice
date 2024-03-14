# 간단한 수학 문제
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, K+1):
    num = N*i
    if N == 1:
        print(K)
        break
    elif num > K :
        print(N*(i-1))
        break