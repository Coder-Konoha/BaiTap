import random
A = {}
rd_str = ''
for i in range(5):
    rd_str = rd_str + random.choice('abcdefghijklmnopqrstuvwxyz')
A['name'] = rd_str.capitalize()
A['age'] = random.randrange(1, 100)