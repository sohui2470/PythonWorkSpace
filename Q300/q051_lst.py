# 051
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 052
movie_rank.append("배트맨")
print(movie_rank)

# 053
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054
movie_rank.remove("럭키")
print(movie_rank)

# 055
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057
nums = []
for i in range(1,8):
    nums.append(i)
print(min(nums))
print(max(nums))

# 058
n = 0
for i in range(1,6):
    n += i
print(n)

# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치전"]
print(len(cook))

# 060
n = 0
for i in range(1, 6):
    n += i
print(n/len(range(1,6)))