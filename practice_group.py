import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("suh 010-1234-5678")
print(m.group("name"))

p1 = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p1.search('Paris in the the spring').group())
