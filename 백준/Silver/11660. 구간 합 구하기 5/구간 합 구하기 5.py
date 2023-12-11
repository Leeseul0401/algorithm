import sys
input = sys.stdin.readline

size, quiz = map(int, input().split())
dp = [[0] * (size + 1) for _ in range(size + 1)]
arr = [[0] * (size + 1)]

for i in range(size):
    input_list = [0] + [int(x) for x in input().split()]
    arr.append(input_list)


for i in range(1, size + 1):
    for j in range(1, size + 1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i][j]
              
for i in range(quiz):
    start_x, start_y, end_x, end_y = map(int, input().split())
    result = dp[end_x][end_y] - dp[start_x - 1][end_y] - dp[end_x][start_y - 1] + dp[start_x - 1][start_y - 1]
    print(result)


