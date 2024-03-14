# coma6863 팀 나누기

import sys

data  = list(map(int, sys.stdin.readline().rstrip().split()))

if sum(data)%2 == 0 :
    print('possible')
else :
    print('impossible')
