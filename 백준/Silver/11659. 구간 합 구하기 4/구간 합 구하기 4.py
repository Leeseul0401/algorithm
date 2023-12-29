import sys
input = sys.stdin.readline

L, Q = map(int, input().split())
arr = list(map(int, input().split()))
sumArr = [0]
temp = 0

for i in arr:
    temp = temp + i
    sumArr.append(temp)
    

for i in range(Q):
    start, end = map(int, input().split())
    print(sumArr[end] - sumArr[start - 1])