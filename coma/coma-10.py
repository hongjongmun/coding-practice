# 기억상실
'''
import sys

A, B, N = map(int, sys.stdin.readline().rstrip().split())
count = 1

while True:
    count += 1
    if A == N:
        break
    A = 2*A-B
print(count)
'''
# 기억상실
import sys
import math

A, B, N = map(int, sys.stdin.readline().rstrip().split())

result = N-A  # 마지막 계산 제거를 위해 총외울 갯수 빼기 하루에 외울수 있는 갯수 3
if result >= N:   
   print(1)
else :
   print(math.ceil((result/(A-B)+1))) # 날짜에는 소수점이 없어서 반올림해서 날짜 계산