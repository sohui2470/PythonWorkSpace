# Q15 Duplicate Numbers
def DuplicateNum(n):
    x = []
    for i in range(10):
        x.append(str(i))
    a = sorted(n)
    if a == x:
        return True
    else:
        return False
print(DuplicateNum(input()))
# copy input() from here>> 0123456789 01234 01234567890 6789012345 012322456789

# (방법2) 해설
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10
print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))