# 세포 A, B
import sys

N = int(sys.stdin.readline().rstrip())

_A= 1
_B= 1
A = 1
B = 2

for i in range(N-1):
    A = _A + A
    B = _B + B 
    _A = A
    _B = B
    print(_A, A, _B, B)
    
print(A, B)

# N A B
# 0 1 1
# 1 1 2
# 2 2 3
# 3 3 5
# 4 5 8
# 5 8 13
# 6 13 21