import requests
import os
import sys

# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Меняем рабочую директорию
os.chdir(script_dir)

direct = 'https://stepik.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as input_data:
    adress = input_data.readline().strip()

r = requests.get(adress)
while r.text.startswith('We') == False:
    next_adress = os.path.join(direct, r.text)
    print(next_adress)
    r = requests.get(next_adress)

print(r.text)