#Шифрование строк
#Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы 
# исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка,
#  которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
def replace_symbols(s, origin, new):
    new_s = ''
    for char in s:
        num_char = origin.find(char)
        new_s = new_s + new[num_char]
    return new_s

symbols = input()
new_symbols = input()
s1 = input()
s2 = input()
res_1 = replace_symbols(s1, symbols, new_symbols)
res_2 = replace_symbols(s2, new_symbols, symbols)
print(res_1)
print(res_2)