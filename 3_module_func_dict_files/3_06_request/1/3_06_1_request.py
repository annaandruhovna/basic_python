import requests
import os
import sys

# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Меняем рабочую директорию
os.chdir(script_dir)

with open('dataset_3378_2.txt') as input_data:
    adress = input_data.readline().strip()

r = requests.get(adress)
list =  r.text.splitlines()
print(len(list))