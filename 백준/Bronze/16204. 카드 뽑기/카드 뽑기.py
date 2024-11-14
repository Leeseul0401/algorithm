N, M, K = map(int, input().split())

A = min(M,K)
B = N - M
C = N - K
result = min(B,C)

print(A + result)