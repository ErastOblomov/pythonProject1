# Функцыи !!!
# найти минимальный четный элемент и разделить все элементы на него
def min_even(l):
    m = l[0]
    for i in l:
        if i < m and i % 2 == 0:
            m = i
    return m

def divide_by_min(l):
    m = min_even(l)
    l1 = []
    for i in l:
        l1.append(i / m)
    return l1

l = [5,2,3,4,5,6,7]
l = divide_by_min(l)
print(l)

# написать функцию, которая принимает словарь и считает сколько ключей представленно в виде строки

def str_key_d(d):
    countK = 0
    for key in d.keys():
        if isinstance(key, str):
            countK += 1
    return countK


d = {1111: 'ffddd', 33: '33333', 'dddd': 33333, 'aasss': 123, '3211': 'dssa'}

d = str_key_d(d)
print(d)

# написать функцию, которая находит все строки в словаре и возврещает из суммарную длину

def stroc(sl):
    length = 0
    for i ,l in sl.items():
        if isinstance(i, str):
            length += len(i)
        if isinstance(l, str):
            length +=len(l)
    return length

print(stroc({'he':1,'hello':3,'sdsfsdf':'kllklk','sdfsdf':'sdfsdfd'}))

#Чтобы подсчитать количество символов в строке Python, мы можем воспользоваться
# циклом for и счётчиком. Тут тоже всё просто, т. к.
# определение длины происходит путём подсчёта числа итераций.
# def findLen(str):
#     counter = 0
#     while str[counter:]:
#         counter += 1
#     return counter
#
# str = "otus"
# print(findLen(str))

# написать функцию, которая принимает неограниченное количество позиционных
# аргуемнтов и находит их среднее арифметическое
def average(*args):
    l = 0
    sred = 0
    for i in args:
        l += i
    sred = l/len(args)
    return sred

print(average(1,2,3,3,3,3,3,3,4,4,4,4,4,44))

# Написать функцию, которая принимает неограниченное
# количество непозиционных элементов и находит среди них, второе по величине число
# def average(**kwargs):
#     print(kwargs)
def vtoroe(**kwargs):
    max = 0
    mi = 0
    for i in kwargs.values():
        if i > max:
            max,mi = i,max
        if i>mi and i<max:
            mi = i
    return mi
print(vtoroe(k = 100,p = 27,f = 4,j=6,h=9,g=12))

#получаем неограниченное число позиционных элементов и ищем среди них самый длинный лист
def vtoroe(*args):
    m = []
    for i in args:
        if isinstance(i, list):
            if len(i) > len(m):
                m = i
    return m
a = vtoroe([1,2,3,4], [11,3,2,5, 6], '123', '12234343')
print(a)