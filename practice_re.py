# 패턴 생성
import re
p = re.compile('[a-z]+')

# match
m = p.match("python")
if m:
    print('Match found: ', m.group())
else:
    print('No match')

# search
m = p.search("python")
print(m)

# finall
result = p.findall("life is too short")
print(result)

# finditer
result = p.finditer("life is too short")
print(result)
for r in result: print(r)

# match 객체의 메서드
m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("suh 010-1234-1234")
print(m.group(0))
print(m.group(1))

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("suh 010-1234-1234")
print(m.group(1))
print(m.group(2))
print(m.group(3))

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

