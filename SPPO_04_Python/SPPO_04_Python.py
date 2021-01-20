#НА ЗАДАНИЕ 1.4
#пРОВЕРКА НА НАБОРЕ 1010001
TCondition = ['p0', 'p1', 'p2', 'p3']
Talpha = ['0', '1']
Tjump = [[0,2], [3,2], [0,2], [3,3]]
Tfinish = ['p2', 'p3']

cond = 'p0'

str = input("Введите строку: ")

for i in str:                           #Если символ не содержится в алфавите, то завершаем программу и выдаем сообщение, что строка не распознана
    if not i in Talpha:
        print('Строка не распознана')
        sys.exit()

for i in str:
    cond = TCondition[Tjump[TCondition.index(cond)][Talpha.index(i)]]   #Движемся по таблице переходов, в соответсвии с введенной строкой
    print(cond)

if cond in Tfinish:                 #Если конечное состояние содержится в TFinish, то строка разпознана, иначе нет
    print('Строка распознана')
else:
    print('Строка не распознана')

input()