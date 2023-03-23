# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5


from random import randint as rnd

numCount = int(input('Введите количество элементов: '))
listNum = []

for i in range(numCount):
    listNum.append(rnd(0, 10))
X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = X - listNum[0]
index = 0
for i in range(1, numCount):
    count = abs(X - listNum[i])
    if count < min:
        min = count
        index = i
print(
    f'Число {listNum[index]} в списке наиболее близко по величине к числу {X}')
print(listNum)
