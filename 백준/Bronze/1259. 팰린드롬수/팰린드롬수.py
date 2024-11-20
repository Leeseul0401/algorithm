import math

while True:
    N = input()
    string_list = list(N)
    
    if '0' == N:
        break
  
    num = math.ceil(len(string_list) / 2)
    
    result = "yes"
    for i in range(num):
        if string_list[i] == string_list[-(i+1)]:
            result = "yes"
        else:
            
            result = "no"
            break
    print(result)
