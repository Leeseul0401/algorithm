N = int(input())
count = 1
T = 1
start_index = 1
end_index = 1

while end_index != N:
    if T == N:
        count = count + 1
        end_index = end_index + 1
        T = T + end_index
        
    elif T < N:
        end_index = end_index + 1
        T = T + end_index
    else:
        
        start_index = start_index + 1
        T = T - start_index
        
    print('count', count)
    print('start_index', start_index)
    print('end_index', end_index)
    print('T', T)
    print()
print(count)



# n = int(input())
# count = 1
# start_index = 1
# end_index = 1
# sum = 1

# while end_index != n:
#     if sum == n:
#         count += 1
#         end_index += 1
#         sum += end_index
#     elif sum > n:
#         sum -= start_index
#         start_index += 1
#     else:
#         end_index += 1
#         sum += end_index

# print(count)