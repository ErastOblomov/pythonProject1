# 1 задача Есть лист чисел. Напишите программу на Python для суммирования всех элементов в списке.

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("вывести лист чисел:")
# print(myList)
# sumElements = 0
# for element in myList:
#     sumElements = sumElements + element
#
# print("сумма элементов:", sumElements)
#2 задача Напишите программу на Python, чтобы получить наибольшее число из списка
# list1 = [3, 22, 8, 5, 110, 65]
# max_number = max(list1)
# print("Наибольшее число:", max_number)

# 3 задача Найти в словаре самое большое число. Искать стоит среди ключей и значений.

d = {"a": 3, "‘b": "hello", "c": 4, "d": -3}
def get_max_int(dict):
    my_list = []
    for i in dict:
        if type(dict[i]) == int or type(dict[i]) == float:
            my_list.append(dict[i])
    return max(my_list)
print(get_max_int(d))

#4 задача Есть список строк, найти строку, в которой есть большая буква

# def is_upper(x):
#     for i in x:
#         if i.isupper():
#             print(x)
#             return
# capital_latter = ['Напишите', 'слово', 'боТ', 'bUss', 'boot']
# for word in capital_latter:
#     is_upper(word)

#5 задача Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)


