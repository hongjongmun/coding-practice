# coma6857 스칼라곱
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
result = []

for i in range(N):
    result.append(A[i]*B[i])
    
print(sum(result))