# 직각 삼각형
import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if (a**2 + b**2) == c**2:
    print('YES')
else :
    print('NO')