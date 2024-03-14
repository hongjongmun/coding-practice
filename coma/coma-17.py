# 주민등록증
import sys

data = sys.stdin.readline().rstrip()

if len(data) > 20:
    print(0)
else :
    print(-1)