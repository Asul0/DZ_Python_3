# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1


from random import randint as rnd

numCount = int(input('Введите количество элементов: '))
listNum = []

for i in range(numCount):
    listNum.append(rnd(0, 10))
inputNum = int(input('Введите число X, которое необходимо найти в списке: '))
count = 0
for j in range(numCount):
    if listNum[j] == inputNum:
        count += 1
print(f'Число {inputNum} встречается в списке {count} раз')
print(listNum)
