import csv
with open('game.txt', encoding='UTF8') as file:
    lines = file.readlines()[1:]
    answer = list()
    ''' открываем текстовый документ и создаем список '''
    for l in lines:
        line = l.split('$')
        if '55' in line[2]:
            print(f'У персонажа {line[1]} в игре {line[0]} нашлась ошибка с кодом: {line[2]}. Дата фиксации: {line[3]}')
            line[2] = 'Done'
            line[3] = '0000-00-00'
        if '\n' in line[3]:
            line[3] = line[3][:-2]
        ''' считывает каждую строку и анализирует на наличие ошибки, далее заменяет ошибку и дату на нужную конструкцию'''
        answer.append(line)
with open('game_new.csv', 'w', encoding='UTF8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['gameName', 'characters', 'errorName', 'date'])
    w.writerows(answer)
    '''создает новый файл с верными данными'''