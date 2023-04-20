#Задача про монетки. Сколько монеток надо перевернуть, чтобы все они лежали одинаково?
print("Задача 1")
import random
countReshka=0
countOrel=0
n = int(input("Введите кол-во монеток  "))
for _ in range(n):
    monetki = random.randint(0, 1)
    print(monetki)
    if monetki==1:
        countReshka +=1
    else:
        countOrel +=1
if countReshka==countOrel:
    print("Невероятно, но здесь все равно, какие монетки переворачивать, кол-во орлов и решек на столе одинаково")
else:
    if countReshka>countOrel:
        #если решек больше, то мы пишем что надо перевернуть CountOrel(количество монеток с орлом сверху)
        print(f"надо перевернуть минимум {countOrel} монеток, чтобы все они лежали одной стороной вверх")
    else:
        print(f"надо перевернуть минимум {countReshka} монеток, чтобы все они лежали одной стороной вверх")

#угадываем два числа зная их произведение и сумму. 
print("Задача 2")
import math
p=int(input("Введите резульат умножения X и Y     ")) #48
s=int(input("Введите резульат сложения X и Y      ")) #16
y=1
x=p//y #48/1
for x in range(p):
    for y in range(s):
        if p==x*y and s==x+y:
            print(f"Ура, наши числа это {x} и {y}")
    

#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N
#  выводить степенидвоцки до того момента, пока степень двоки не превзойдет N
print("Задача 3")
N=int(input("Введите N  "))
result=0
y=0
while result< N:
    result=2**y
    y+=1
    if result<N:
        print(result)
    
