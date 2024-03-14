# 비밀번호 찾기

import sys

data = input().split()
key = []

for i in data:
    key.append(i)
    if i == 'c':
        break    

print(*key)