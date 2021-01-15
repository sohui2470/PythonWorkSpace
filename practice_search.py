# 문제 06.하위 디렉토리 검색하기
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:              
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("c:/python_space")

# 하위 디렉토리 검색을 윕게 해주는 os.walk
# 시작 디렉토리부터 그 하위 모든 디렉터리를 차례대로 방문하는 함수
import os

for(path, dir, files) in os.walk("c:\python_space"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == 'py':
            print("%s/%s" % (path, filename))