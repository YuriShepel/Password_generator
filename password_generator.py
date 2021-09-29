import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
number_pass = int(input('Введите количество необходимых паролей: '))
number_char = int(input('Введите количество символов для пароля: '))
ness_digit = input('Нужно ли включить цыфры в пароль? д - Да, н - Нет')
ness_apper = input('Включать ли заглавные буквы? д - Да, н - Нет')
ness_lower = input('Включать ли строчные буквы? д - Да, н - Нет')
ness_punct = input('Включать ли символы? д - Да, н - Нет')
exc_ambig = input('Исключать ли неоднозначные символы il1Lo0O? д - Да, н - Нет')
if ness_digit == 'д':
    chars += digits
if ness_apper == 'д':
    chars += uppercase_letters
if ness_lower == 'д':
    chars += lowercase_letters
if ness_punct == 'д':
    chars += punctuation
if exc_ambig == 'д':
    for c in 'il1Lo0O':
        chars.replace(c, '')