# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
A = int(input("введите число А   "))
B = int(input("Введите число В   "))


def result(A, B):
    A += 1
    B -= 1
    if B > 0:
        return result(A, B)
    else:
        return A

print(result(A, B))