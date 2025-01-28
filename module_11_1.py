import numpy as np
import pandas as pd

'''
Библиотека Numpy
Создать массив чисел, выполнить мат операции с массивами и вывести результат в консоль.
'''
# Создание массива чисел
arr_1 = np.arange(1, 10).reshape(3, 3)
print(arr_1)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Сумма всех чисел массива:
print(arr_1.sum()) # 45
# Минимальное число в массиве:
print(arr_1.min()) # 1
# Максимальное число в массиве:
print(arr_1.max()) # 9
# Обращение к элементу по индексу:
print(arr_1[1][2]) # 6
# Срез
print(arr_1[2:]) # [[7 8 9]]
# Сложение двух массивов
arr_2 = arr_1.transpose() # транспонирование
print(f'{arr_1}\n + \n{arr_2} \n= \n{arr_1 + arr_2}')

'''
Библиотека Pandas
Считать данные из файла, выполнить простой анализ и вывести результат в консоль.
'''
# Создание дата-сета из CSV-файла с данным о расходах и доходах за год
journal = pd.read_csv("journal.csv", sep=",")
# Добавление нового столбца
journal["inc - exp"] = journal["income"] - journal["expenses"]
print(journal)
# Простой анализ данных
print(f'Максимальный доход за месяц: {journal["income"].max()}')
print(f'Минимальный расход за месяц: {journal["expenses"].min()}')
print(f'Прибыль за год: {journal["inc - exp"].sum()}')