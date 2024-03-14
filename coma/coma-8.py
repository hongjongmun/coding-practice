# 자녀의 키 구하기

import sys
import math

data = list(map(int, sys.stdin.readline().rstrip().split()))

result = (data[0] + data[1]) / len(data)
print(math.trunc(result))

