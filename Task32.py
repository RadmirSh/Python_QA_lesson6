# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

lst = [1, 5, 10, 3, 7, 2, 8]
# Задаем диапазон значений
min_val = 3
max_val = 7

# проверка принадлежности элемента заданному диапазону, вывод результата
for i in range(len(lst)):
    if min_val <= lst[i] <= max_val:
        print(i, end=' ')