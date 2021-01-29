# 041
ticker = "btc_krw"
print(ticker.upper())

# 042
print(ticker.lower())

# 043
word = "hello"
print(word.capitalize())

# 044
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 045
for i in ['xlsx','xls']:
    if file_name.endswith(i):
        print("end with", i, True)
        break

# 046
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 047
a = "hello world"
print(a.split())

# 048
ticker = "btc_krw"
print(ticker.split('_'))

#049
date = "2020-05-01"
print(date.split('-'))

# 050
data = "039490  "
print(data.rstrip())