# 031
# 34

# 032
# HiHiHi

# 033
print('-'*80)

# 034
t1 = "python"
t2 = "java"
print((t1 +' '+ t2 + ' ')*3)

# 035
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 037
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 038
num = "5,969,782,550"
list = num.split(',')
a = int(''.join(list))
print(a, type(a))

# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040
data = "   삼성전자    "
data = data.strip()
print(data)
