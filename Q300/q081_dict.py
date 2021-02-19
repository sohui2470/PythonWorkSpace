# 081
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*a, b, c = scores
valid_score = a
print(valid_score)

# 082
a, b, *c = scores
valid_score = c
print(valid_score)

# 083
a, *b, c = scores
valid_score = b
print(valid_score)

# 084
temp = {}
print(type(temp))

# 085
ice = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(ice)

# 086
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)

# 087
print("메로나 가격:", ice['메로나'])

# 088
ice['메로나'] = 1300
print(ice)

# 089
del ice['메로나']
print(ice)

# 090
# 오류 발생 원인: 없는 인덱스 호출