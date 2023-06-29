import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
K = 0
count = 0
numbers.sort()

for k in range(N):
    find = numbers[i]
    i = 0
    j = N - 1
    while i < j: # 투 포인터 알고리즘
        if numbers[i] + numbers[j] == find:
            if i != k and j != k:
                    count = count + 1
                    break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif numbers[i] + numbers[j] < find:
            i += 1
        else:
            j -= 1
print(count)