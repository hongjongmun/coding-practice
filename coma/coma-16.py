# 최대공약수

import sys

N, M= map(int, sys.stdin.readline().rstrip().split())

# 값이 더 큰건 M
if N > M:
    N, M = M, N

num_N = []
num_M = []

# 각각 약수 구하기
for i in range(1, N+1):
    if N % i == 0:
        num_N.append(i)
        
for i in range(1, M+1):
    if M % i == 0:
        num_M.append(i)
        
# 최대공약수 찾기(두 리스트 같은 값 찾고 내림차순 후 첫번째 값)
result = list(set(num_N) & set(num_M))
result = sorted(result, reverse=True)

print(result[0])