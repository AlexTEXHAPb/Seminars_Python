# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# X = abs(int(input('Введите первое натуральное число: ')))
# Y = abs(int(input('Введите второе натуральное число: ')))
# S = X + Y
# print(f'Первая подсказка: сумма чисел равна - {S}')
# P = X * Y
# print(f'Вторая подсказка: произведение чисел равно - {P}')
# x = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# y = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# print(f'Ответ: первое число равно {x}, второе {y}.')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по 
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для 
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате 
# отгадать задуманные Петей числа.

# print('Введите два натуральных числа от 1 до 1000')
# X = abs(int(input('Первое число: ')))
# Y = abs(int(input('Второе число: ')))
# S = X + Y
# print(f'Первая подсказка: сумма чисел равна - {S}')
# P = X * Y
# print(f'Вторая подсказка: произведение чисел равно - {P}')
# count = 0
# for i in range(1001):
#     if count != 1:
#         for j in range(1001):
#             if count != 1:
#                 if i * j == P and i + j == S:
#                     print(f'Ответ: первое число равно {i}, второе {j}.')
#                     count = 1
#         else:
#             j = 1001
#     else:
#         i = 1001

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = abs(int(input('Введите число N - ')))
print(f'Целые степени числа 2 от 1 до {N}:')
count = 0
n = 2
for i in range(N):
    if count != 1:
        n = n ** i
        if n <= N:
            print(n, end=' ')
            n = 2
        else:
            count = 1
    else:
        i = N