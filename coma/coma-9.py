# 삼각형의 조건
import sys

num = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for i in num:
    if i > 0:
        result += i
    else :
        print('F')
if result == 180:
    print('P')
else :
    print('F')