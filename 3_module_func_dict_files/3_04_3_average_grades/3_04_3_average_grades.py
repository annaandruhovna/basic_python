import os
import sys
# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# Меняем рабочую директорию
os.chdir(script_dir)

def mean(data):
    n = len(data)
    sum = 0
    for d in data:
        sum += int(d)
    return sum / n

grades = []
aver_grade_person = []
count_person = 0
with open('dataset_3363_4.txt', encoding="utf-8") as table:
    for line in table:
        grade = line.strip().split(';')
        del grade[0]
        aver = mean(grade)
        aver_grade_person.append(aver)
        grades.append(grade)
        count_person += 1

    

    
    with open('3_average_grades.txt', 'w') as result:
        for aver in aver_grade_person:
            result.write(str(aver)+'\n')
        
        for j in range(count_person):
            column = [row[j] for row in grades]
            aver = mean(column)
            result.write(str(aver)+ ' ')