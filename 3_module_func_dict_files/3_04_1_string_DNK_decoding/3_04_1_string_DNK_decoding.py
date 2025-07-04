import os
import sys

# Получаем абсолютный путь к текущему .py-файлу
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Меняем рабочую директорию
os.chdir(script_dir)

with open('dataset_3363_2.txt') as file_1:
    for line in file_1:
        n = len(line)
        check_symb = []
        for char in line:
            if char.isdigit():
                check_symb.append(0)
            else:
                check_symb.append(1)
        decoding_line = ''
        i = 0
        while i < n:
            if check_symb[i] == 1:
                symbol = line[i]
                num = ''
                i += 1
                while (check_symb[i] != 1) and (i < n - 1):
                    num = num + line[i]
                    
                    i += 1
                    if i == n - 1:
                        break
                repeat_symbol = symbol * int(num)
                decoding_line = decoding_line + repeat_symbol
                if i == n - 1:
                    break
    with open('3_decoding_result.txt', 'w') as result:
        result.write(decoding_line)
