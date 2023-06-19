import sys
input = sys.stdin.readline

size, quiz = map(int, input().split())
dp = [[0 for j in range(size + 1)] for i in range(size + 1)]
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









# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# A = [[0] * (n + 1)]
# D = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
    
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
#     print(result) 
