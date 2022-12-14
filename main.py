# Реализуйте классы MinStat, MaxStat, AverageStat, которые
# будут находить минимум, максимум и среднее арифметическое
# последовательности целых чисел.
# Экземпляры классов инициализируются без аргументов.
# Метод add_number должен добавлять в статистику число, которое
# будет учтено при вычислении финального результата методом result.
# Для экземпляров MinStat и MaxStat result должен возвращать
# целое число, для AverageStat — число типа float (это число будет
# сравниваться с правильным ответом до седьмой значащей цифры).
#
# Если в последовательности отсутствуют числа и статистические
# величины вычислить невозможно, метод result должен возвращать None.


# class MinStat:
#     def __init__(self):
#         self.num = []
#
#     def result(self):
#         return min(self.num)
#
#     def add_number(self, n):
#         self.num.append(n)
#
# class MaxStat:
#     def __init__(self):
#         self.num = []
#
#     def result(self):
#         return max(self.num)
#
#     def add_number(self, n):
#         self.num.append(n)
#
# class AverageStat:
#     def __init__(self):
#         self.num = []
#
#     def result(self):
#         if self.num == None:
#             return None
#         else:
#             s = sum(self.num)
#             l = len(self.num)
#             av = s/l
#             return av
#
#     def add_number(self, n):
#         self.num.append(n)
#
#
# num = [1, 2, 4, 6]
# min_num = MinStat()
# max_num = MaxStat()
# average = AverageStat()
# for i in num:
#     min_num.add_number(i)
#     max_num.add_number(i)
#     average.add_number(i)
#
# print(min_num.result(),';', max_num.result(),';', '{:<05.3}'.format(average.result()))


# Реализуйте класс Table, который хранит целые числа в двумерной
# таблице. При инициализации Table(rows, cols) экземпляру
# передаются число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля.
# table.get_value(row, col) — прочитать значение из ячейки
# в строке row, столбце col. Если ячейка с индексами row и col
# не лежит внутри таблицы, нужно вернуть None.
#
# table.set_value(row, col, value) — записать число в ячейку
# строки row, столбца col. Гарантируется, что в тестах
# будет в запись только в ячейки внутри таблицы.
#
# table.n_rows() — вернуть число строк в таблице
#
# table.n_cols() — вернуть число столбцов в таблице
#
# table.delete_row(row) — удалить строку с номером row
#
# table.delete_col(col) — удалить колонку с номером col
#
# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.
#
# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.

# class Table(object):
#
#     def __init__(self, col, row):
#         self.col = col
#         self.row = row
#         self.table = [[0] * col for i in range(row)]
#
#     def set_value(self, row, col, num):
#         self.table[row][col] = num
#
#     def n_rows(self):
#         return self.row
#
#     def n_cols(self):
#         return self.col
#
#     def delete_col(self, col):
#         self.table[col] = self.table.pop(col)
#         self.col -= 1
#         return self.table[col]
#
#     def delete_row(self, row):
#         self.table[row] = self.table.pop(row)
#         self.row -= 1
#         return self.table[row]
#
#     def add_row(self, row):
#         self.table.insert(row, [0] * self.col)
#         self.row += 1
#
#     def add_col(self, col):
#         for row in range(self.row):
#             self.table[row].insert(col, 0)
#         self.col += 1
#
#     def get_value(self, col, row):
#         if 0 <= row < self.row and 0 <= col < self.col:
#             return self.table[row][col]
#         else:
#             return None
#
#
# tab = Table(2, 2)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(0)
# tab.add_col(1)
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()