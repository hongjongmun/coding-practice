# 쉬운 암호화

import sys

# 한개의 정수 입력 받기
num = int(sys.stdin.readline().rstrip())
result = []

for i in range(num):
    for j in range(num):
        if i * j == num:
            result.append(i)
            result.append(j)

# 리스트 중복 제거
result = list(set(result))
# 오름차순 정렬
result.sort()
print(result)
count = 0
# 리스트 안의 숫자가 소수인지 아닌지 판별
for i in result:  # [3, 5]
    a = 0
    for j in range(2, i):
        if i % j == 0:
            a = 1
            continue
    if a == 1:
        result.remove(i)
        count = 1
        continue
        
if count == 0:
        print(result[0], end=' ')   
        print(result[1])       
else :            
    print('IMPOSSIBLE')
   