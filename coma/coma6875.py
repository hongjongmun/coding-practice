# 소수점 이진비트

import sys

a = float(sys.stdin.readline().rstrip())
result = '0.'
stop = 0

num = a*2
i_ = int(num) # 정수부분
f_ = num - i_ # 소수부분
    
# print(i_, f_)
i_ = str(i_)
result = result+i_

if f_ == 0.0:
    stop = 1

for i in range(9):
    if stop == 1:
        break
    num = f_*2
    i_ = int(num) # 정수부분
    f_ = num - i_ # 소수부분
      
    # print(i_, f_)
    i_ = str(i_)
    result = result+i_
    # print(f_== 0)
    if f_ == 0.0:
        break
    
print(result)