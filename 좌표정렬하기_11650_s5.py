import sys
input = sys.stdin.readline
N = int(input())


# numbers = [[0 for j in map(int, input().split())] for i in range(N + 1)] 써도 틀려
numbers = [[0 for j in range(2)] for i in range(N + 1)]

for i in range(N):
    x, y = map(int, input().split())
    numbers[i][0] = x
    numbers[i][1] = y

# sort 써도 틀림
    
for i in range(N):
    if numbers[i][0] == numbers[i+1][0]:
        if numbers[i][1] > numbers[i+1][1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            
    elif numbers[i][0] > numbers[i+1][0]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
numbers.remove([0,0])

print(numbers)

# 다른사람 답

# import sys
# input = sys.stdin.readline
# n = int(input())

# array = []
# for i in range(n):
#     [a, b] = map(int, input().split())
#     array.append([a,b])
    
# s_array = sorted(array)

# for i in range(n):
#     print(s_array[i][0], s_array[i][1])

## 숏 코딩

# for i in sorted([[*map(int,s.split())]for s in open(0)][1:]):print(*i)