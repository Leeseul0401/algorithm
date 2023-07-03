import sys
input = sys.stdin.readline

def _round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
N = int(input())
scores = []

for i in range(N):
    scores.append(int(input()))

scores.sort()

scores.remove(max(scores))
scores.remove(min(scores))

print(round(sum(scores)/len(scores)))

# round 함수는 4사 5입 (4이하는 버리고 5이상부터는 반올림) 이 아니라, 5사 5입(ROUND_HALF_EVEN or dount_to_nearest_even: 앞자리가 홀수면 올라가고 앞자리가 짝수면 버린느 방법) 기반


# import sys
 
# def my_round(val):
#     return int(val) + 1 if val - int(val) >= 0.5 else int(val)
 
# input = sys.stdin.readline
# n = int(input())
# if n:
#     arr = [int(input()) for _ in range(n)]
#     arr.sort()
#     nn = my_round(n * 0.15)
#     print(my_round(sum(arr[nn:-nn] if nn else arr) / (n - 2 * nn)))
# else:
#     print(0)