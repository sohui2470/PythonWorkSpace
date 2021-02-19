# # 코드 1. 정확도 통과, 효율성 미통과
# def solution(participant, completion):
#     answer = []
#     for i in participant:
#         r = participant.count(i) - completion.count(i)
#         if i not in completion:
#             answer.append(i)
#         elif r > 0:
#             answer.append(i)
#             r -= 1
#             participant.remove(i)
#     return ''.join(answer)

# # 코드 2. 정확도 통과, 효율성 미통과
# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     return ''.join(participant)

# # 효율성 통과 풀이: 해시
# def solution(participant, completion):
#     answer =''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#     return answer

# 효율성 통과 풀이: 가장 간결
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(	["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(	["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))