# 서버에 들어온 데이터 수
import sys

import sys
N = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# print(data)

ns = []
ew = []

for i in range(N):  
    
    D = data[i][0]
    X = data[i][1]
      
    if D == 1: # 북쪽
        n_d = X
        ns.append(n_d)
    elif D == 2: # 동쪽
        e_d = X
        ew.append(e_d)
    elif D == 3: # 남쪽
        s_d = -X
        ns.append(s_d)
    else: # 서쪽
        w_d = -X
        ew.append(w_d)

print(sum(ns), sum(ew))