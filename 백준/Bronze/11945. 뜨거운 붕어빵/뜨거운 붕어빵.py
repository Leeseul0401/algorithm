N, M = map(int, input().split())
numbers = [0 for i in range(M)]
for i in range(N):
    numbers = list(input())
    for j in range(M, 0, -1):
        print(numbers[j - 1], end="")
    print()