a = str(input())

# 전체길이
print(len(a))

# 공백제거 후 길이
b = a.replace(' ', '')
print(len(b))

# 단어 개수
c = a.split(' ')
count = 0
for i in c:
    if i != '':
        count += 1
print(count)