# Спики колекцыя
# ввод списка с клавы
# n = 5
# for i in range(n):
#     a.append(input())
#
#
# # посчитать количество целых чисел в списке
# a = [1, 2, 3, '123', 1, None]
# count = 0
# for i in a:
#     if isinstance(i, int):
#         count += 1
# print(count)
#  узнать какое слово само длинное
a = []
count = 0
s = 'I love python'
a = s.split(' ')
m = a[0]
for i in a:
    if len(i) > len(m):
        m = i
print(i)
