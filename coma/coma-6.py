# 가장 큰 나머지
num = int(input())
# 5으로 나눈 나머지
r1 = num % 5
# 7으로 나눈 나머지
r2 = num % 7

if r1 > r2:
    print(r1)
else :
    print(r2)