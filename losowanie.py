
import random

i = 0
fob = open('C:/Users/Sylwek/PycharmProjects/strukdanych/a.txt', 'w')
while i <= 30000:
    a = random.randint(0, 30000)

    fob.write(str(a) + '\n')

    i += 1

fob.close()
