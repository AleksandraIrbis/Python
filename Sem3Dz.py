# Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X.
import random
print("задача 1")
N = int(input("Введите количество элементов    "))
n = int(input("введите проверяемое число   "))
array = [random.randint(0, 100) for i in range(N)]
res = 0
for item in array:
    if item == n:
        res += 1
print(array, res, sep='\n')

# Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X
N = abs(int(input('Введите количество элементов списка А: ')))
numbers = [random.randint(0, 10) for i in range(N)]
X = int(input('Введите проверяемое число'))
razn1 = abs(X - numbers[0])
index = 0
for i in range(1, N):
    razn2 = abs(X - numbers[i])
    if razn2 < razn1:
        razn1 = razn2
        index = i
print(numbers)
print(f"ответ {numbers[index]}")