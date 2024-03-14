# over_nuderflow
import sys

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

result = n1 + n2

if result > 7:
    result = result - 16
elif result < -8:
    result = result + 16

print(result)