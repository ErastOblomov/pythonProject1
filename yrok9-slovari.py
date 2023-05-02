# a = [1, 2, 3, 4]
# d = {'Ivanov':'Ivan', 'Petrov':'Petr'}
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)
#
# for key, value in d.items():
#     print(key, value)

# # задача: найти пары, где ключ длиннее значения
# ma = {'ivan': 'ivvvvan', 'ivadddddn': 'ivffffffffffvvvan', 'ivfan1231qwds2qwdqwdqw': 'ivvvjjjjjjjvan',
#       'ivean': 'ivvvvvvvvan', }
# for key, value in ma.items():
#     if len(key) > len(value):
#         print(key, value)
#
# # задача :   посчитать где больше значений типа int, среди ключей или значений
ma = {1:'ivvvvan','ivadddddn':2,3:3,'ivean':'ivvvvvvvvan',}
countKey = 0
countValues = 0
for i in ma.keys():
    if isinstance(i, int):
        countKey+=1
for i in ma.values():
    if isinstance(i, int):
        countValues+=1
