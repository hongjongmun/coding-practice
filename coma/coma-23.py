# 여러 줄 입력받기

import sys
s1 = []

for i in range(2):
    s1.append(sys.stdin.readline().rstrip().split('\n'))

print(s1[0][0])
print(s1[1][0])