N = input()
# club = ['MatKor','WiCys','CyKor','AlKor','$clear']


# matching = [s for s in club if N in s] 
# print(matching)
if N == 'M':
    print('MatKor')
elif N == 'W':
    print('WiCys')
elif N == 'C':
    print('CyKor')
elif N == 'A':
    print('AlKor')
elif N == '$':
    print('$clear')