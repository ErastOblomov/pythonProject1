str='пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'
if str.islower(): # проверяем с моленьких символов строка если да то
 print(str.capitalize()) # Начните строку с заглавной буквы, если она находится в нижнем регистре.
print(str.find('сопровождать')) #Найдите индекс вхождения подстроки ‘сопровождать’.
print(str.replace('сопровождать','поддерживать')) #Замените вхождение подстроки ‘сопровождать’ на ‘поддерживать’.
print(str.split(','))     # Разбейте предложение на части по запятым.
print(','.join(str.split(',')))  #Соедините части обратно, снова добавив запятые между частями.