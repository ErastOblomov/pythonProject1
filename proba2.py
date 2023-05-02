n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
a = list(map(int, input().split()))[:n]
print(a)
m=a[0]
mn=a[1]
for i in range(1, len(a)):
     if a[i-1]>0 and m < mn :
         m = a[i]
         mn = a[i-1]
     m=mn
     mn=a[i+1]

print(mn,end='')

l = list()
n = int(input("введите  число элементов массива \n"))
print('введите сам массив через пробел')
list = list(map(int, input().split()))[:n]
for i in range (n):
    if list[i] > 0:
        l.append(list[i])
l.sort()
print(l[0])



