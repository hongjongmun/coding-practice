# 난수 생성
import sys

X, A, B, C, N = map(int, sys.stdin.readline().rstrip().split())

# 난수 생성 반복
for i in range(N):
    X = ((X*A) + B) % C
print(X)    
