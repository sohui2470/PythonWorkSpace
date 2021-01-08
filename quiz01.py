# 문제 https://wikidocs.net/42526

#  Q1 평균점수 구하기
gildong = {'국어':80, '영어':75, '수학':55}
scores = list(gildong.values())
sum=0
for i in [0,1,2]:
    sum += scores[i]
print(sum/len(scores))

# Q2 홀짝 판별
i=13
if((i%2)==0):
    print('짝수')
else:
    print ('홀수')

# Q3
id = '881120%s1068234' %"-"
print(id[:6])
print(id[7:])
# yyyymmdd = id[:6]
# num = id[7:]
# print(yyyymmdd)
# print(num)

# Q4
pin = "881120-1068234"
print(pin[7:8])
# print(pin[7])

# Q5
a = "a:b:c:d"
print(a.replace(":","#"))

# Q6
li = [1,3,5,4,2]
li.sort()
li.reverse()
print(li)

# Q7
q7 = ['Life', 'is', 'too', 'short']
print(" ".join(q7))

# Q8
t1 = (1, 2, 3)
t2 = 4,  # comma 없이는 오류 발생
print(t1 + t2)

# Q9 객관식
# 3번, 딕셔너리의 key값은 불변해야 한다.
# [1]은 리스트이므로 변함. 따라서 불가능.

# Q10
a = {'A':90, 'B':80, 'c':70}
print(a.pop('B'))

# Q11
a = [1,1,1,2,2,3,3,3,4,4,5]
b = set(a)
print(b)

# Q12 주관식
# a = b= [1,2,3]
# a[1]=4
# print(b)
# 참조하는 객체가 동일함 (a is b >>>true 이므로)
# b의 두 번째 요솟값도 변경되어 있음을 확인할 수 있다.
