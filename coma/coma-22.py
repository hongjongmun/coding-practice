# k 개수 구하기

import sys

s = sys.stdin.readline().rstrip()
count = 0

for i in range(len(s)):
    if s[i] == 'k':
        count += 1
        
print(count)