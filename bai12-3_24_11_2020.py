import random
n = random.randint(50, 100)
A = []
for i in range(n):
    rd_str = ''
    for a in range(random.randint(1, 6)):
        rd_str = rd_str + random.choice('abcdefghijklmnopqrstuvwxyz')
    A.append({'name':rd_str.capitalize(), 'age': random.randint(1, 100)})