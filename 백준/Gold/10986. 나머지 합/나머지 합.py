import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m     # 길이가 나머지니까 m보다 클 수 없어서 길이를 m으로 해둠
S[0] = A[0]     # 합 배열 첫 번째 값은 (0번 인덱스) 여기서 초기화 해주고 밑에서 1번 인덱스부터 연산해줌
answer = 0

for i in range(1, n):  
    S[i] = S[i-1] + A[i]    # 합 배열 저장

for i in range(n):
    remainder = S[i] % m    # 합 배열의 모든 값에 % 연산 수행
    if remainder == 0:
        answer += 1
    C[remainder] += 1       # 나머지가 같은 인덱스의 개수 값 증가시키기
    
for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)
        
print(answer)