import os
import sys
import time
start_time = time.time()  # время начала выполнения

# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Меняем рабочую директорию
os.chdir(script_dir)

#word_set = set()
#full_text = []
dictionary = {}
with open('dataset_3363_3.txt') as file_2:
    for line in file_2:
        sentence = line.lower().split()
        for word in sentence:
            if dictionary.get(word) is None:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
            #word_set.add(word)
            #full_text.append(word)

max_value = max(dictionary.values())
n = len(dictionary.values())
max_words = []
for key, value in dictionary.items():
    if value == max_value:
        max_words.append(key)
max_words.sort()
print(max_words[0], max_value)

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")