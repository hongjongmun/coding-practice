n = int(input())
s1 = 0
for i in range(1, n+1):
    s1 += i
    if s1 >= n:
        print(i)
        break