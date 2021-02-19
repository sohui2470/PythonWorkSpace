# # 효율성 fail
# def solution(arr):
#     count = 0
#     answer = arr[:]
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             print(i)
#             del answer[i-count]
#             count += 1
#     return answer

# 효율성 통과, but not best sol.
def solution(arr):
    answer = []
    copy = arr[1:]
    for i in range(len(copy)):
        if arr[i] != copy[i]:
            answer.append(arr[i])
    if arr[-1] == copy[-1]:
        answer.append(arr[-1])    
    return answer

# 누군가의 엄청난 풀이
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer



print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))