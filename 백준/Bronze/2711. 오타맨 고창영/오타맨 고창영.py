N = int(input())

for i in range(N):
    idx, message = map(str, input().split())
    result = message[:int(idx)-1] +  message[int(idx):]
    print(result)