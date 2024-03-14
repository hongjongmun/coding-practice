n = int(input())

# 리스트로 저장하기
a = input().split()

# 리스트 각 요소 값 정수 변환
for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')