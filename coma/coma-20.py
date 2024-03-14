# 1~N까지 숫자 중 5의 배수 개수 출력
import sys

N = int(sys.stdin.readline().rstrip())
count = 0

for i in range(1, N+1):
    if i % 5 == 0:
        count += 1
    else :
        continue
    
print(count)