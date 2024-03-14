# 모든수들의 합
import sys

num_s = []
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    data = input()
    num_s.append(data)
        
num_i = list(map(int, num_s))
print(sum(num_i))