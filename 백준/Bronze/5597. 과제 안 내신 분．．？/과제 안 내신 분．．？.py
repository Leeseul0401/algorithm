a = list(range(1,31))

for i in range(28):
    num = int(input())
    if num in a:
        a.remove(num)

print(a[0])
print(a[1])