# 8진수와 16진수
num = int(input())
a1 = []
n1, n2 = 0, 0
b, c = num, num
# 8진수 변환
for i in range(100):
    if b != 0:
        n1 = b % 8
        b = b // 8   
        a1.append(n1)
    else :
        break
a1.reverse()
print(''.join(map(str, a1)), end=' ')

# 16진수 변환
dic = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
a2 = []
for i in range(100):
    if c != 0:
        n1 = c % 16
        c = c // 16   
        a2.append(n1)
    else :
        break
a2.reverse()
for i in range(len(a2)):
    if a2[i] > 9:
        a2[i] = dic.get(a2[i])
print(''.join(map(str, a2)))
