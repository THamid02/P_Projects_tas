import random

number = "0123456789"
symbol = "!@#$%^&*()"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

all = lower + upper + symbol + number
length = 12
password = "".join(random.sample(all, length))
print(password)
