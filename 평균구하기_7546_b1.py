N = int(input())
numbers = list(map(int, input().split()))
avg = 0
sum = 0
M = 0

for i in numbers:
    if M < i:
        M = i
        
    sum = sum + i
    avg = sum * 100 / M / N
    
print(avg)

# 책 정답

# n = input()
# mylist = list(map(int, input().split()))
# mymax = max(mylist)
# sum = sum(mylist)
# print(sum * 100 / mymax / int(n))