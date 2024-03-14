# 원의 넓이 구하기

import sys

num = int(sys.stdin.readline().strip())
result = (num**2)*3.14
if result == 314.0:
    print('%g' %(result))
else:
    print(result)