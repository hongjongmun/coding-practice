# 거울
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if a > b :
    max_n = a
else :
    max_n = b
    
max_n = str(max_n)
max_n = ''.join(reversed(max_n))
print(max_n)