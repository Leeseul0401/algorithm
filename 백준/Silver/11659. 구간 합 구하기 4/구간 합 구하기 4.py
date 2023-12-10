import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sum_list = [0]
temp = 0

for i in numbers:
    temp = temp + i
    sum_list.append(temp)
    
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(sum_list[e] - sum_list[s - 1])    
