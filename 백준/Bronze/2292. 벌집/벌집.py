n = int(input())

hive = 1 # 벌집 갯수, 1부터 시작
cnt = 1

while n > hive:     # n = 1, hive = 1 => while문 안돌아
                    # n = 2, hive = 1, cnt = 1,  n = 13, hive = 1 / 7 / 12,
    hive += 6 * cnt # 6배수로 증가  ,hive = 6    ,  hive = 6 -> 12 -> 18
    cnt += 1        # 반복문을 반복하는 횟수 ,cnt = 2, cnt = 2 -> 3 -> 4

print(cnt)
    