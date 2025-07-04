import os
import sys

def mean(a):
    result = sum(a) / len(a)
    return result
# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# Меняем рабочую директорию
os.chdir(script_dir)

height_class = {str(i): [] for i in range(1,12)}

with open('dataset_3380_5.txt', encoding="utf-8") as table:
    for line in table:
        inform = line.strip().split()
        height_class[inform[0]].append(int(inform[2]))

with open('result.txt', 'w') as result:
    for key, heights in height_class.items():
        if len(heights) != 0:
            aver = str(mean(heights))
        else:
            aver = '-'
        result_string = key + ' ' + aver
        result.write(str(result_string)+'\n')