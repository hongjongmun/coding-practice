# 학점
import sys

a = int(sys.stdin.readline().rstrip())

if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
else :
    print('F')