# 소수 구하기

import sys

num = int(sys.stdin.readline().rstrip())
result = []

for i in range(2, num+1):
    data = []
    for j in range(1, num+1):
        if i % j == 0:
            data.append(j)
    if len(data) == 2:
        result.append(1)
        
print(len(result))