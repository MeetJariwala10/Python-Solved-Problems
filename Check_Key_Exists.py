''' Check whether a given key is present or not in a dictionary '''

d = {1: 10, 2: 25, 3: 30, 4: 45, 5: 50, 6: 65}

def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
      
is_key_present(5)
is_key_present(9)
