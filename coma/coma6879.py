# 팰린드롬
import sys

month, day = map(int, sys.stdin.readline().rstrip().split())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
stop = 0
for i in range(2):
    for j in range(day+1, months[month-1]):
        A = str(month+count)
        B = str(j)
        if len(B) == 1:
            B_ = '0'+B
        else :
            B_ = B
        C = A + B_
        # 문자열을 리스트로
        C_ = list(C)  
        # 리스트 역순으로
        C_.reverse() 
        # 리스트를 문자열로
        C_ = ''.join(C_)
        # print(C)
        # print(C_)
        
        if C == C_:
            print(A, B)
            stop = 1
            break
    if stop == 1:
        break
    if month == 12:
        month = 0
    day = 0
    count += 1

# 1 01   10 01  11 11  12 21 
# 1 11   
# 1 21
# 1 31

# 2 02
# 2 12
# 2 22

# 3 03
# 3 13
# 3 23

# 4 04
# 4 14
# 4 24

# 5 05
# 5 15
# 5 25

# 6 06
# 6 16
# 6 26

