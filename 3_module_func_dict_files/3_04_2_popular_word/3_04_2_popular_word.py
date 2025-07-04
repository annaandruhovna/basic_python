import os
import sys
import time
start_time = time.time()  # время начала выполнения

# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Меняем рабочую директорию
os.chdir(script_dir)

word_set = set()
full_text = []
with open('dataset_3363_3.txt') as file_2:
    for line in file_2:
        sentence = line.lower().split()
        for word in sentence:
            word_set.add(word)
            full_text.append(word)
    
    d = {}
    for word in word_set:
        count = full_text.count(word)
        if d.get(count) is None:
            d[count] = [word]
        else:
            d[count].append(word)
    
max_count = max(d.keys())
min_word = min(d[max_count])
print(min_word, max_count)

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")