N = int(input())
result = 0

for i in range(N):
    try:
        M = input()
        M = list(M)
        result = M.count('S')
        #newList = [x for x in M if 'L' in M]
        result2 = 0
        if 'L' in M :
            result2 = ( M.count('L') // 2 ) + 1
        
        #print('result : ', result,'result2 : ', result2,'result + result2 : ', result + result2)
        
        print(result + result2)
    except EOFError:
        break