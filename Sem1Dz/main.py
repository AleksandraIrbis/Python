#Найдите сумму цифр трехзначного числа.
print("Задача 1")
n=int(input("Введите проверяемое число"))
sum=0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print(sum)



#Задача про Катю, Сережу и Петю
print("Задача 2")
import math
suma=int(input("Введите общее количество журавликов"))
serg=petya=suma//6
katya=2*(serg + petya)
print(serg, petya, katya)

#проверить введенное число на счастливость: сумма трех первых чисел равна сумме трех последних. всего чисел 6
print("Задача 3")
ticket=(input("введите шестизначное число      ")) 
if len(ticket)==6:
     sum1=int(ticket[0])+int(ticket[1])+int(ticket[2])
     sum2=int(ticket[3])+int(ticket[4])+int(ticket[5])
     if sum1==sum2:
         print("Ура, вам попался счастливый билетик!")
     else:
         print("Увы, вам не повезло, попробуйте в другой день(((((")
         # 385916
else:
     print("Это не шестизначное число, повторите попытку")

#Делим шоколадку на дольки
print("Задача 4")
poloska = int(input("Сколько полосочек у шоколадки?    "))
stolbik = int(input("сколько столбиков у шоколадки?    "))
kusok = int(input("сколько кусочков  шоколадки ты хочешь быстро отломить у другана и сбежать?     "))
if kusok < poloska*stolbik and (kusok%stolbik==0 or kusok%poloska==0):
    print("хватай и беги!")
else:
    print("Ну тут постараться придется, друган точно успеет заметить и надавать тебе по лапам)))))")
