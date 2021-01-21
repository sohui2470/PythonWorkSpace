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

# (해설) 방법 2
data = "4546793"
numbers = list(map(int, data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:
        is_odd = num % 2 == 1
        is_next_odd = numbers[i+1] % 2 == 1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")
        
print("".join(result))