''' Combine multiple dictionaries into a single dictionary '''


dic1 = {1 : 15, 2 : 25}
dic2 = {3 : 30, 4 : 40}
dic3 = {5 : 50,6 : 65, 7 : 70}

dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)

print(dic4)
