# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062
nums = []
for i in range(1,11):
    if i % 2 == 1:
        nums.append(i)
print(nums)
# 방법 2
nums = []
for i in range(1,11):
    nums.append(i)
print(nums[::2])

# 063
nums = []
for i in range(1,11):
    nums.append(i)
print(nums[1::2])

# 064
nums = [1,2,3,4,5]
print(nums[::-1])

# 065
i = ['apple', 'banana', 'cocomong']
print(i[0], i[2])

# 066
print(''.join(i))

# 067
print('/'.join(i))

# 068
print('\n'.join(i))

# 069
string = "apple/banana/cocomong"
interest = string.split('/')
print(interest)

# 070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)