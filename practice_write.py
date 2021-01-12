f = open("c:\python_space\\new.txt", 'w')
for i in range(1,11):
    # write = "%d번째 줄입니다.\n" % i
    f.write("%d번째 줄입니다.\n" % i)
f.close()

f = open("c:\python_space\\new.txt","r")
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close

f = open("c:\python_space\\new.txt","a")
for i in range(11,20):
    f.write("%d번째 줄입니다.\n" % i)
f.close

with open("new2.txt", 'w') as f:
    f.write("practice")