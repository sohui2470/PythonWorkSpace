# 문제 https://wikidocs.net/42527

# Q1 주관식
# shirt

# Q2
sum=0
i=1
while i <= 1000:
    if i%3==0:
        sum = sum+i
    i+=1
print(sum)

# Q3
# a=1
# while(a<=5):
#     print("*"*a)
#     a +=1
t=1
while True:
    print("*"*t)
    if(t==5):
        break
    t+=1


# Q4
for i in range(100):
    print(i+1)

# Q5
score = [70, 65, 55, 75, 95, 90, 80, 85, 100]
sum=0
for p in range(9): # 길이 맞추기 유의
    sum += score[p]
print(sum / len(score))
# for p in score:
#     sum += p  #어차피 리스트에서 하나씩 나오므로 더 간단
# print(sum / len(score))

# Q6
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)