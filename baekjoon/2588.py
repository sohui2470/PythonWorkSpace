n1 = int(input())
n2 = input()
n3 = n1*int(n2[2])
n4 = n1*int(n2[1])
n5 = n1*int(n2[0])
n6 = n3+n4*10+n5*100
print(n3)
print(n4)
print(n5)
print(n6)

# 누군가의 더 짧은 풀이
a = int(input())
b = list(map(int, list(input())))
for i in range(3):
    print(a*b[2-i])
print(a*(100*b[0]+10*b[1]+b[2]))