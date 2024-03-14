# DNA
import sys

N = int(sys.stdin.readline().rstrip())

DNA = str(input())
# print(DNA)

for i in DNA:
    if i == 'A':
        print('T', end='')
    elif i == 'T':
        print('A', end='')
    elif i == 'G':
        print('C', end='')
    else :
        print('G', end='')