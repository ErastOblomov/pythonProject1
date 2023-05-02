#Есть лист чисел. Напишите программу на Python для суммирования всех элементов в списке.

#myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("вывести лист чисел:")
# print(myList)
# sumElements = 0
# for element in myList:
#     sumElements = sumElements + element
#
# print("сумма элементов:", sumElements)
l = [1,2,3,4,5]
sum = 0
for i in l:
    sum += i
print(sum)


#Напишите программу на Python, чтобы получить наибольшее число из списка
#list1 = [3, 22, 8, 5, 110, 65]
# max_number = max(list1)
# print("Наибольшее число:", max_number)

l = [1,2,3,4,5]
max = l[0]
for i in l:
    if i > max:
        max = i
print(max)

# Найти в словаре самое большое число. Искать стоит среди ключей и значений.
# d = {"a": 3, "‘b": "hello", "c": 4, "d": -3}
# def get_max_int(dict):
#     my_list = []
#     for i in dict:
#         if type(dict[i]) == int or type(dict[i]) == float:
#             my_list.append(dict[i])
#     return max(my_list)
# print(get_max_int(d))
l = {1:1, 3:3, 5:8 , 2:2}
max = -100000000
for key, value in l.items():
    if isinstance(key, int):
        if key > max:
            max = key
    if isinstance(value, int):
        if value > max:
            max = value

print(max)

# Есть список строк, найти строку, в которой есть большая буква
# # def is_upper(x):
#     for i in x:
#         if i.isupper():
#             print(x)
#             return
#
#
# capital_latter = ['Напишите', 'слово', 'боТ', 'bUss', 'boot']
# for word in capital_latter:
#     is_upper(word)

l = ['sdmfksmf', 'wqeQQkmkm', 'qweq']

for i in l:
    for j in i:
        if j.isupper():
            print(i)
            break

#5 задача  Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
# a = [int(i) for i in input().split()]
# num_distinct = 1
# for i in range(0, len(a) - 1):
#     if a[i] != a[i + 1]:
#         num_distinct += 1
# print(num_distinct)

lit = list(map(int, input().split())) [:1000]
l = []
count = 0
for i in range (len(lit)):
    if lit.count(i) == 1:
        count += 1
print("Ответ ", count)