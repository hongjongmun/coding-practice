# # 분해합
# import sys

# N = int(sys.stdin.readline().rstrip())

# for i in range(1, 10):
#     Na = N - i

# # 1~9까지의 값들로 완전탐색 적용
# num_list = list(map(int, str(N)))

# # 결과값 출력
# result = sum(num_list) + N
# print(sum(num_list))
# print(N)
# print(result)

# N = int(input())

# min_result = 0
# sum_result = 0

# for i in range(N-1,N-len(str(N))*9-1,-1):
#   for j in str(i):
#     sum_result += int(j)
#   if N == i + sum_result:
#     min_result = i
#   sum_result = 0

# print(min_result)

# 256
N = int(input())

min_result = 0
sum_result = 0

# i는 입력한 숫자 -1 부터 입력한 숫자 - 자릿수까지 -1만큼한다.
for i in range(N-1,N-len(str(N))*9-1,-1):

  if i>0:
    for j in str(i):
      sum_result += int(j)
    if N == i + sum_result:
      min_result = i
    sum_result = 0

print(min_result)
