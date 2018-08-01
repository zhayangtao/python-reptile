import re


pattern = re.compile(r'\d+')
result1 = re.match(pattern, '192abc')
if result1:
    print(result1.group())
else:
    print('failed')

result2 = re.match(pattern, 'abc192')
if result2:
    print(result2.group())
else:
    print('failed2')

result3 = re.search(pattern, 'abc192efdf')
if result3:
    print(result3.group())
else:
    print('failed3')
# re.findall
print(re.findall(pattern, 'A1B2C3D4'))



