import random
n = random.randrange(5,10)
A = []
for i in range(n):
    rd_str = ''
    for a in range(5):
        rd_str = rd_str + random.choice('abcdefghijklmnopqrstuvwxyz')
    A.append({'name':rd_str.capitalize(), 'age': random.randint(1, 100)})