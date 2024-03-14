# 암호 해독
import sys

pw = str(sys.stdin.readline().rstrip())
id = 0
result = pw[0]
stop = 0

if len(pw) == 1:
    stop = 1

try:
    for i in range(1, len(pw)):
        if stop == 1:
            break
        id = id + i
        result = result + pw[id]
    print(result)
except IndexError:
    print(result)
        
# print(result)
#  1 2 3 4
# 0 1 3 6 10
# v rr rrr ffff nnnnn