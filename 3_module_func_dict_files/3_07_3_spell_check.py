#Проверка орфографии
#На вход программе первой строкой передаётся количество d известных нам слов, 
# после чего на d строках указываются эти слова. Затем передаётся количество l строк текста
#  для проверки, после чего l строк текста.
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

def input_words(count_words):
    correct_words = []
    
    for i in range(count_words):
        word = input().lower()
        correct_words.append(word)
    return correct_words

wrong_words = set()
#Ввод коррекных слов
count_words = int(input())
correct_words = input_words(count_words)
#Ввод предложений, которые нужно проверить
count_strings = int(input())
input_strings = input_words(count_strings)

#Для каждой введенной на проверку строки
for str in input_strings:
    #Разбить на слова
    words = str.split()
    #Для каждого слова
    for word in words:
        #Если слова нет в списке
        if word not in correct_words:
            wrong_words.add(word)
for word in wrong_words:
    print(word)