N = int(input())
M = int(input())
resource = list(map(int, input().split()))
resource.sort()
start_index = 1
end_index = N - 1
count = 0

while start_index < end_index:
    sum = resource[start_index] + resource[end_index]
    if sum < M :
        start_index += 1
    elif sum > M:
        end_index -= 1
    else:
        count = count + 1
        start_index += 1
        end_index -= 1
        
print(count)


# import sys
# input  = sys.stdin.readline
# N = int(input())
# M = int(input())
# A = list(map(int, input().split()))
# A.sort()
# count = 0
# i = 0
# j = N - 1

# while i < j:
#     if A[i] + A[j] < M:
#         i += 1
#     elif A[i] + A[j] > M:
#         j -= 1
#     else:
#         count += 1
#         i += 1
#         j -= 1
        
# print(count)