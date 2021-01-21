# 021
letters = 'python'
print(letters[0])
print(letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
a = []
string = list(string)
while(len(string)>0):
    n = string.pop()
    if n == "홀":
        a.append(n)
print(''.join(a))
# 다른 방법
string = "홀짝홀짝홀짝"
print(string[::2])

# 024
string = "PYTHON"
print(''.join(reversed(string)))
# 다른 방법
string = "PYTHON"
print(string[::-1])

# 025
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

# 026
print(phone_number.replace('-',''))

# 027
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split)
print(url_split[-1])

# 028
lang = "python"
# lang[0] = 'p'     # TypeError: 'str' object does not support item assignment 
print(lang)
# 

# 029
string = 'abcdfe2a354a43a'
string = string.replace('a','A')

# 030
string = 'abcd'
string.replace('b', 'B')
print(string)
# 원본은 변하지 않으므로 abcd 출력