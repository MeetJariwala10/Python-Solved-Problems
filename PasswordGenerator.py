import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/_-"

add = lower + upper + numbers + symbols

length = 16

password = "".join(random.sample(add, length))
print(password)