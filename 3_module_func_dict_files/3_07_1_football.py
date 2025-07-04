#Вывод информации о футбольных командах по их матчам
#Напишите программу, которая принимает на стандартный вход 
# список игр футбольных команд с результатом матча и выводит
#  на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, 
# за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет 
# n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;
# Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков


points = {'win': 3, 'draw': 1, 'loss': 0}
data = {}
count_games = int(input())
for i in range(count_games):
    game = input().split(';')
    teams = [game[0], game[2]]
    goals = [int(game[1]), int(game[3])]
    tables = [[1, 0, 0, 0, 0],[1, 0, 0, 0, 0]]
    i = 0
    if goals[i] == goals[i+1]:
        for j in range(2):
            tables[j][2] = 1
            tables[j][4] = points['draw']
    else:
        if goals[i] > goals[i+1]:
            num_win = i
            num_loss = i + 1
        else:
            num_win = i + 1 
            num_loss = i                   
        tables[num_win][1] = 1
        tables[num_win][4] = points['win']
        tables[num_loss][3] = 1
        tables[num_loss][4] = points['loss']

    for i in range(2):
        if data.get(teams[i]) is None:
            data[teams[i]] = tables[i]
        else:
            #Сложение двух списков поэлементно через генераторы списков
            data[teams[i]] = [x + y for x, y in zip(data[teams[i]], tables[i])]

for key, values in data.items():
    str_output = key+':'
    for value in values:
        str_output = str_output + ' '
        str_output = str_output + str(value)
    print(str_output)