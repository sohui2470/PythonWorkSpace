# 071
my_variable = ()
print(type(my_variable))

# 072
movie_rank = ('drstrange', 'split', 'lucky')

# 073
memo = (1, )
# 튜플에 하나만 저장하려면 쉼표 입력해야 함

# 074
t = (1,2,3)
# t[0] = 'a' -> 오류
# 튜플은 원소 값 대입, 수정 불가능

# 075
t = 1,2,3,4
print(type(t))
# 튜플은 괄호 없이도 입력 가능

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
# 변경 불가하므로 새로 정의해야 함

# 077
interest = ('academy', 'bio', 'culture')
interest = list(interest)

# 078
interest = ['academy', 'bio', 'culture']
interest = tuple(interest)

# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a,b,c)

# 080
t = tuple(range(2, 100, 2))
print(t)