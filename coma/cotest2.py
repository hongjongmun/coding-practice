# 장군의 땅

import sys
import numpy as np

a, b = map(int, sys.stdin.readline().rstrip().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(a)]
data = np.array(data)
print(data)

result = []
# 1번째 땅 모양의 경우의 수 구하기
for i in range(a-1): # 행이동
    for j in range(b-1): # 열이동
        result.append(sum(sum(data[i:i+2, j:j+2])))   # 0:2, 0:2 # 0:2, 1:3 # 0:2, 2:3
print(result)
        
# 1번째 그림의 필터
#print(sum(sum(data[0:2, 0:2])))
# print('-'*10)
# # 2번째 그림의 필터
# print(sum(data[0, :]))
# print('-'*10)
# # 3번째 그림의 필터
# print(data[0][1])
# print(sum(data[1, 0:3]))
# print('-'*10)
# # 4번째 그림의 필터
# print(data[0][0])
# print(sum(data[1, 0:3]))
# print('-'*10)
# # 5번째 그림의 필터
# print(sum(data[0, 0:3]))
# print(data[1][0])
# print('-'*10)
# # 6번째 그림의 필터
# print(sum(data[0, 0:2]))
# print(sum(data[1, 1:3]))
# print('-'*10)