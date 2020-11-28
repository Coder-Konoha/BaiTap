import random
A = {}
rd_str = ''
for i in range(random.randint(1, 6)):
    rd_str = rd_str + random.choice('abcdefghijklmnopqrstuvwxyz')
A['name'] = rd_str.capitalize()
A['age'] = random.randint(1, 100)