# 첫째항 3 두항의 차이 5   7번째 항 출력

data = list(map(int, input().split() ) )

a = data[0]
b = data[1]
n = data[2]

for i in range(n-1):
    a = a + b

print(a)