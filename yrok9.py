#Ввести массив строк и найти там строку, в которой больше всего маленьких буков
a = ['asQEJaa', 'asdasQQQds', 'aaa']
s = ''
loc_count = 0
max_count = 0
for i in a:        # перебор строк в масиве
    for j in i:    # перебор букв в строке
        if j.islower(): # проверка  символа на маленький
            loc_count += 1  # увеличиваем счетчик  маленьких элементов в строке
    if loc_count > max_count:  # проверка если счетчик мал.элементов больше максимального  то
        s = i                  # в S присваиваем  адрес масива строки i
        max_count = loc_count  #  увеличиваем  счетчик  количества маленьких элементов в строке
    loc_count = 0              # сбрасываем  счетчик для проверки следующей строки количество мал. элементов
print(s)