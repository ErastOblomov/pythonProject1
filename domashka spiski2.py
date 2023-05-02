#1 дан массив чисел . выведите все элементы массива ,которые больше предыдущего элемента
n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
a = list(map(int, input().split()))[:n]  # будет принимать строку, преобразовывать ее в список строк,
# а затем преобразовывать каждый элемент этого списка в целые числа. и [:n]возвращает
# n элементы списка, предполагая, что он n содержит число. нашего целочисленного списка.
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
     print(a[i])
# 2 вариант
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(1,n,1):
    if a[i] > a[i-1]:
        print(a[i])


#2  дан массив целых чисел если в нем 2 соседних элемента одного знака
#выводим эти числа , если соседних элементов одного знака нет  ни чего не выводим
#если таких пар соседей несколько -выводим 1ю пару
n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
a = list(map(int, input().split()))[:n]
m=0

for i in range(1, len(a)):
    while m < 1:
        if a[i] > 0 and a[i - 1]>0 :
            print(a[i-1],a[i])
        elif a[i]< 0 and a[i - 1]< 0:
            print(a[i-1],a[i])
        m+=1
        if m==1:
          break
# второй вариант
n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
a = list(map(int, input().split()))[:n]
m=0

for i in range(1, len(a)):
    if a[i] * a[i - 1] > 0 :
        print(a[i-1],a[i])
        break
# задача 3
n= int(input())
ma = []
m = 2100000000
for p in range(n):
    ma.append(int(input()))

for i in ma:
    if i > 0 and i < m:
        m = i
print(m)

#  задача 4
n= int(input())
ma = []
m = 2100000000
for p in range(n):
    ma.append(int(input()))

for i in ma:
    if i%2 != 0 and i < m:
        m = i
print(m)
# задача 5
n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
a = list(map(int, input().split()))[:n]
for i in range(1, n, 2):
    a[i-1], a[i] = a[i], a[i-1]
print("Ответ ", a)

#задача 6
l = a()
n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
a = list(map(int, input().split())) [:n]
for i in range(n):
    if a.count(a[i]) == 1:
       print(a[i])