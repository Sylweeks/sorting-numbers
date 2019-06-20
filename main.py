import time
from statistics import median
import csv

czas = []         #lista z czasami
instances = []   #lista z instancjami
config=[]
f = open("config.txt")
for line in f:
    config.append(line.strip('\n'))
    #instancje = int(f.readline().strip())
    #wejsciowy = f.readline()
    #print(instancje)
lines = []
print(config[0])
print(config[2])
print(config[3])
instancje = int(config[0])
wejsciowy = config[2]
wyjsciowy = config[3]

fr = open(wejsciowy, 'r')
#fr = open('C:/Users/Sylwek/PycharmProjects/strukdanych/a.txt', 'r')
for line in fr:
    lines.append(int(line.strip('\n')))
fr.close()


def quickSort(lines):

    if len(lines) == 1 or len(lines) == 0:
        return lines
    else:
        pivot = lines[0]
        i = 0
        for j in range(len(lines)-1):
            if lines[j+1] < pivot:
                lines[j+1],lines[i+1] = lines[i+1], lines[j+1]
                i += 1
        lines[0],lines[i] = lines[i],lines[0]
        first_part = quickSort(lines[:i])
        second_part = quickSort(lines[i+1:])
        first_part.append(lines[i])
    return first_part + second_part




def babel(lines):
   for i in range(len(lines)-1,0,-1):
       for j in range(i):
           if lines[j] > lines[j+1]:
               temp = lines[j]
               lines[j] = lines[j+1]
               lines[j+1] = temp
   return lines

a = input("Wybierz co zrobic\n1.Sortowanie babelkowe\n2.Sortowanie szybkie\n")

if a == "1":
    print("sortowanie babelkowe")
    lines[instancje-10000:] = []
    dl = len(lines)
    czasinstancji = []
    i = instancje-10000
    while i > 0:

        for j in range(2):
            start = time.time()
            babel(lines)
            end = time.time()
            print(end-start)
            czasinstancji.append(end - start)
        instances.append(len(lines))
        i -= 1000
        lines[i:] = []
        czas.append(median(czasinstancji))
        print(czas, instances)


    fw = open('C:/Users/Sylwek/PycharmProjects/strukdanych/b.txt', 'w')
    fw.write(str(lines))
    fw.close()
    with open(wyjsciowy, 'a', newline='') as plik:
        fieldnames=['czas','instancja']
        wr = csv.writer(plik,delimiter=',')
        wr.writerow(czas)
        wr.writerow(instances)

elif a == "2":
    print("sortowanie szybkie")
    lines[instancje:] = []
    dl = len(lines)
    czasinstancji = []
    i = instancje

    while i > 0:
        for j in range(20):
            start = time.time()
            quickSort(lines)
            end = time.time()
            print(end-start)
            czasinstancji.append(end-start)
        instances.append(len(lines))
        i -= 500
        lines[i:] = []
        czas.append(median(czasinstancji))
        print(czas,instances)


    fw = open('C:/Users/Sylwek/PycharmProjects/strukdanych/b.txt', 'w')
    fw.write(str(lines))
    fw.close()

    with open(wyjsciowy, 'a', newline='') as plik:
        fieldnames=['czas','instancja']
        wr = csv.writer(plik,delimiter=',')
        wr.writerow(czas)
        wr.writerow(instances)


#gra w znajdywanie slow, dostaniemy slowa, maja sie ukladac w ten kwadrat
#struktura + operacje dodaj /usun, generujemy plansze> parametry>liczba slow ukrytych, minimalna liczba skrzyżowań,okreslona wielkosc planszy> kwadrat>kierunki czytania
#rozwiazywanie wyszukiwanie wzorca metoda naiwna karpa-rabina>>>10 na 40
#na 7 MAJA


