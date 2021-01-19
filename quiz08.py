# Q1 문자열 바꾸기
x1 = 'a:b:c:d'
x2 = x1.split(':')
x3 ="#".join(x2)
print(x3)

# Q2 딕셔너리 값 추출하기
try:
    a = {'A':90, 'B':80}
    print(a['C'])
except KeyError:
    print(70)
# 다른 방법(해설)
a = {'A':90, 'B': 80}
print(a.get('C', 70)) # 해당 key 가 없을 경우 두 번째 매개변수로 전달된 default 값을 반환

# Q3 리스트의 더하기와 extend 함수
a = [1,2,3]
print(id(a))
a = a + [4,5]
print(id(a))
a = [1,2,3]
a.extend([4,5])
print(id(a))
# 차이점은? id()값이 + [4,5]를 하면 바뀌지만(즉, 새로운 리스트 반환), extend시에는 유지된다.

 # Q4 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i>=50:
        sum += i
print(sum)
# (방법 2)
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
print(result)

# Q5 피보나치 함수
def fun(n):
    num = 0
    list = [0,1]
    val = list[num]+list[num+1]
    while (val <= n):
        list.append(val)
        num += 1
        val = list[num]+list[num+1]
    return list
    
print(fun(10))
print(fun(30))

# (방법 2) 해설: 재귀함수 이용
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i), end=' ')

# Q6 숫자의 총합 구하기
a = input().split(',')
b = list(map(int, a))
sum = 0
for i in b:
    sum += i
print (sum)

# Q7 한 줄 구구단
n = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
i = 1
while(i<10):
    print(n*i, end=" ")
    i += 1

# Q8 역순 저장
f = open('abc.txt', 'w')
f.write("AAA\nBBB\nCCC\nDDD\nEEE")
f.close()

f = open('abc.txt', 'r')
content = f.readlines()
f.close()
content.reverse()
new=[]
for i in content:
    new.append(i.replace("\n",""))

f = open('abc.txt', 'w')
for i in range(len(new)):
    f.write(new[i]+"\n")
f.close()

# 복잡하게 제거하고 삽입하는 대신에
# (방법2) 해설
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

# Q9 평균값 구하기
f = open('sample.txt', 'w')
f.write('70\n60\n55\n75\n95\n90\n80\n80\n85\n100')
f.close()

f = open('sample.txt', 'r')
line = f.readlines()
f.close()

n =[]
for i in line:
    n.append(i.replace('\n', ''))
intlist = list(map(int, n))

sum = 0
for i in intlist:
    sum += i
average = sum/len(intlist)

f = open('result.txt', 'w')
f.write("%d" % average)
f.close()

# replace할 필요 없이 score = int(line)으로 끝남
# 해설지 풀이
f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score  = int(line)
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()

# Q10 사칙연산 계산기
class Calculator:
    def __init__(self, x):
        self.x = list(x)
    def sum(self):
        a = 0
        for i in self.x:
            a += i
        return a
    def avg(self):
        return self.sum()/len(self.x)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

# Q11 모듈 사용 방법
# 명령 프롬프트의 import 목록에 c:\doit을 추가한다

# Q12 오류와 예외 처리(주관식)
# 7

# Q13 DashInsert 함수
def DashInsert(n):
    try:
        a = []
        x = []
        j = 1
        for i in range(len(n)):
            a.append(int(n[i]))
            x.append(int(n[i]))

        for i in range(len(a)-1):
            print(a)
            # print(i,"~", i+1, end = ',')
            # print(a[i]%2 == 1 and a[i+1] % 2 == 1)
            # print(a[i]%2 == 0 and a[i+1]%2 == 0)
            if a[i]%2 == 0 and a[i+1]%2 == 0 :
                print("i =", i, "일 때 홀수가 연속됩니다.")
                x.insert(i+j,'*')
                print(x)
                j += 1
            elif a[i]%2 == 1 and a[i+1] % 2 == 1:
                print("i =", i, "일 때 짝수가 연속됩니다.")
                x.insert(i+j,'-')
                print(x)
                j += 1
            else:
                print('i =', i, "는 해당되지 않습니다.")
                pass
    except TypeError:
        print("i =",i, "에서 오류가 발생합니다.")
    result = ''.join(map(str, x))
    return result
print(DashInsert('4546793'))


# Q14 문자열 압축하기
x = input()
# x = 'aaabbcccccca' # 예제 3,2,6,1 len = 12
x = list(x)
print(x)
count = []
i = 0
con = 1
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        con += 1
        print(con)
    else:
        count.append(con)
        con = 1
if i+1 == len(x)-1:
    count.append(con)
print(count)

a = []
j = 0
for i in count:
    a.append(x[j] + str(i))
    j += i
print(a)

print(''.join(a))


for i in x:
    count.append(x.count(i))
print(count)
i = 0
a = []
while(i<len(count)):
    a.append(x[i] + str(count[i]))
    i += int(count[i])
print(a)

# Q15 Duplicate Numbers
def DuplicateNum(n):
    x = []
    for i in range(10):
        x.append(str(i))
    a = sorted(n)
    if a == x:
        return True
    else:
        return False
print(DuplicateNum(input()))
# copy input() from here>> 0123456789 01234 01234567890 6789012345 012322456789

# Q16 모스 부호 해독


# Q17 기초 메타 문자 (객관식)
# 2

# Q18 문자열 검색 (주관식)
import re
p = re.compile('[a-z]+')
m =  p.search("5 python")
print(m.start()+print(m.end())
# 2 + 8 = 10

# Q19 그루핑
contact = "park 010-1234-1234"
import re
p = re.compile(r"(?P<name>\w+\s+)(?P<tomiddlenum>\d+[-]\d+[-])(?P<lastnum>\d+)")
m = p.search(contact)
value = m.group("lastnum")
print(p.sub('\g<name>\g<tomiddlenum>####', contact))

# Q20 전방 탐색
email = "sohui2470@gmail.co.kr"
import re
p = re.compile(r".*[@].*[.](?=^com$|^net$).*$")
m = p.search(email)
print(m)

