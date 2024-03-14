import sys

a, b = map(int, sys.stdin.readline().rstrip().split()) # 2, 5

fivo = [1, 1]
fivo_fivo = [1, ]

# 피보나치
for i in range(b-2): # 숫자 총 3개 추가
    p = fivo[i]+fivo[i+1] # 첫째항과 둘째 항 덧셈
    if len(fivo) > b:
        break
    fivo.append(p)
    
# print(fivo)

# 피보나치 피보나치
for i in range(1, b):
    pp = fivo[i]
    for j in range(fivo[i]):
        if len(fivo_fivo) > b:
            break
        fivo_fivo.append(pp)

# print(fivo_fivo)
print(sum(fivo_fivo[a-1:b]))
