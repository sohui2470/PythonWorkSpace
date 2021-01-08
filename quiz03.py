# 04장 연습문제 https://wikidocs.net/42528

# Q1 홀짝판별
number = input()
def is_odd(number):
    if (number%2==0):
        return "even"
    else:
        return "odd"

# 람다와 조건부 포현식 사용해 한줄로 만들기
is_odd1 = lambda x: "even" if x % 2 == 0 else "odd"

# Q2 입력값 평균계산
def average(*list):
    sum = 0
    for i in list:
        sum += i
    average = sum/len(list)
    return average

# Q3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %d 입니다" % total)

# Q4 객관식
print("you" "need" "python") # 큰따옴표""가 +역할을 함

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# close 를 명시할 필요 없는 with 구문으로 표현시
with open("test.txt",'w') as f1:
    f1.write("Life is too short!")
with open("test.txt", 'r') as f2:
    print(f2.read())

# Q6
f3 = open("test02.txt", 'a')
f3.write(input())
f3.close

# Q7
# 제시문 삽입
f4 = open("test03.txt", 'w')
f4.write("Life is too short\n")
f4.write("you need java")
f4.close

# 변경 후 저장
f4 = open("test03.txt", 'r')
lines = f4.read()
modify = lines.replace("java", "python")
f4.close

f4 = open("test03.txt", 'w')
f4.write(modify)
f4.close