d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(20):
    a = list(map(int, input().split()))
    for j in range(20):
        d[j][i] = a[j]

print(d)