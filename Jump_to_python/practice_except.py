try:
    4/0
except ZeroDivisionError as e:
    print(e)

f = open('new.txt', 'w')
try:
    f.write("hey!")
finally:
    f.close()

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    b = [3,4]
    print(b[5])
    5/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    c = [5,6]
    print(c[6])
    6/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

try:
    f = open("nofile",'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()

# 예외 만들기; 오류 클래스
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    # pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
# except MyError:
    # print("허용되지 않는 별명입니다.")
