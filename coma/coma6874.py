# 비밀번호
import sys, re

pw = str(sys.stdin.readline().rstrip())
pw_1 = re.sub('[a-z]', ' ', pw)
# print(pw_1)
# print(pw)

data = pw_1.split()
data_ = list(map(int, data))
print(sum(data_))