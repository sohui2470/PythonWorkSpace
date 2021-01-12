import sys
sys.path
sys.exit
sys.path.append("C:\python_space\mymod")

# pickle: 객체의 형태 유지하면서 파일에 저장하고 불러오는 모듈
import pickle
f = open("new.txt",'wb')
data = {1: 'python', 2:'you need'}
pickle.dump(data,f)
f.close()

import pickle
f = open("new.txt", 'rb')
data = pickle.load(f)
print(data)

import os
os.environ
os.environ['PATH']
# os.chdir() 디렉토리 위치 변경
# os.getcwd() 디레토리 위치 반환
os.system("dir") # 시스템 명령어 호출
f = os.popen("dir") # 시스템 명령어 결과값 돌려받기
print(f.read())

import shutil # 파일복사
shutil.copy("new.txt", "new_copy.txt")

import glob # 디렉터리에 있는 파일 리스트로 만들기
g = glob.glob("c:\python_space\quiz*")
print(g)

import tempfile # 중복되지 않는 임시 파일명 무작위로 만들어줌
filename = tempfile.mkstemp()
print(filename)

f = tempfile.TemporaryFile() # 임시저장공간으로 사용할 객체: 'wb'모드가 기본
f.close()

import time
print(time.time()) # 현재시간을 실수 단위로 돌려줌
print(time.localtime(time.time())) # 연월일시분초
print(time.asctime(time.localtime(time.time()))) #알아보기 쉽게
print(time.ctime()) # asctime(현재시간)을 간략히 호출 가능
print(time.strftime('%x',time.localtime(time.time())))

for i in range(10):
    print(i)
    time.sleep(0.1) # 일정한 시간(초)간격으로 루프 실행

import calendar
print(calendar.calendar(2021))
calendar.prcal(2022)
calendar.prmonth(2020, 1)
calendar.weekday(2020,12,31)
calendar.monthrange(2021,1)

import random
random.random()
random.randint(1,20)
random.randint(1,80)
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

def radom_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

data = [1,2,3,4,5]
random.shuffle(data)
print(data)

import webbrowser
webbrowser.open("http://drive.google.com")
webbrowser.open_new("http://photos.google.com")