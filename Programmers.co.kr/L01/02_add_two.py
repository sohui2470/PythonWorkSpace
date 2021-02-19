def solution(numbers):        
    x = []
    answer = []
    for i in numbers:
        for j in numbers:
            x.append(i+j)
        x.remove(i+i)
    for i in x:
        if i not in answer:
            answer.append(i)
    answer.sort()
    return answer

print(solution([5,0,2,7]))