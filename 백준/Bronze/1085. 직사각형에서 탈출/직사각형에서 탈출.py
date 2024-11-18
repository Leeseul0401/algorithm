x, y, w, h = map(int, input().split())

resultX = abs(x - w)
resultY = abs(y - h)

if resultX > x:
    resultX = x

if resultY > y:
    resultY = y

print(min(resultX, resultY))