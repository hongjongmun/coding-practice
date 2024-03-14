# 림보게임
import sys
P = 'P'
I = 'I'
N = int(input())
data = list(map(int, sys.stdin.readline().strip().split()))
count = 0

for i in range(len(data)):
    count += 1
    if data[i] > 160:
        continue
    elif i <= 160:
        print(f'{I} {data[i]}')
        count -= 1
        break
if count == len(data):
    print('P')