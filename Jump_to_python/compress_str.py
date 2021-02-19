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

# (방법2) 해설
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))