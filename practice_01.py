# 문제 01. 2단 출력
def GuGu(n):
    result = []
    for i in range(9):
        result.append(n*(i+1))
    return result

print(GuGu(2))

# 문제 02. 3과 5의 배수 합하기
def sumAll(number):
    sumi = []
    sumj = []
    i = number // 3
    j = number // 5
    for i in range(i):
        sumi.append(3*(i+1))
    for j in range(j):
        sumj.append(5*(j+1))
    sumset = set(list(sumi + sumj))
    a = 0
    for k in sumset:
        a += k 
    return a

print(sumAll(1000))

# 선생님 풀이
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0: # or로 연결해야 중복되지 않음
        result += n

print(result)

# 문제 03. 게시판 페이징하기
def getTotalPage(m, n):
    if (m%n == 0):
        return (m // n)
    else:
        return (m // n)+1

print(getTotalPage(12,5))
