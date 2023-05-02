# # # #Есть лист со строками. Вводим букву. Посчитать сколько раз данная буква встретилась в листе
# # s = ['hello', ' word',' name']
# # b = input()
# # max = 0
# # for i in s:
# #     max += i.count(b)
# # print(max)
# #
# #
# # # Есть лист со строками. найти самую часто встречающуюся букву
# #
# # s = ['kjhhfа', 'fjhkhkб', 'lkjjjjllkjв', 'llkhjgjgfd', 'sddsaaaд', 'lkjhе']
# # s1=''
# # for i in s:
# #     s1 += i
# #     count = 0
# #     m = ''
# #     for i in s1:
# #         if i.isalpha() and s1.count(i) > count:
# #             m = i
# #             count = s1.count(i)
# #
# # print('самая часто встречающуюся букву в листе: \n',m)
#
#
# # есть лист числе, найти в нем второй по величине элемент
# # 1 2 3 4 5
# # 4
# s=['1','2','3','4','5']
# s.sort()
# print(s[-2])
# # вариант 2
#
s = [2, 3, 5, 0, 0, 4]
max = 0
premax = 0
if s[0] > s[1]:
    max = s[0]
    premax = s[1]
else:
    max = s[1]
    premax = s[0]
for i in s:
    if i > max:
        premax = max
        max = i
    elif i > premax:
        premax = i
print(premax)
#
# # вариант  3
#
# s=[1, 2, 3 , 4 ,5]
# j=0
# jmax=0
# for i in s:
#     if j<i:
#         j, i= i, j
#         if j> jmax:
#             jmax, j=j, jmax
#
# print (j)

# # найти количество локальных максимумов в листе чисел
# s = [3, 2, 3, 1, 2, 1]
# count = 0
# for i in range(1, len(s)-1):
#     if s[i] > s[i-1] and s[i] > s[i+1]:
#         count += 1
# print(count)


# # найти количество локальных максимумов в листе чисел
# x = int(input())
# lst = []
# while x != 0:
#     lst.append(x)
#     x = int(input())
# print(max(lst), lst.count(max(lst)))
