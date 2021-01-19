# Q20 전방 탐색
email = "sohui1234@gmail.com"
import re
p = re.compile(r".*[@].*[.](?=com$|net$).*$")
m = p.match(email)
print(m)

# (답)
import re

pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))
