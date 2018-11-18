# Hard
#
# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

text = input('Введите текст: ')

text_result = []
count_words = 0
count_latinica = 0

for char in text:
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        count_latinica+=1
    if char.isalpha() or char.isspace():
        text_result.append(char)

text_result=str(''.join(text_result))
count_words = len(text_result.split())

print('===Статистика по тексту===')
print('1. количество слов в тексте: ', count_words)
print('2. количество латинский букв в тексте: ', count_latinica)


# Задача-2
# Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах.
# Без учета регистра

def split_text(text):
    """
    переводит текст в нижний регистр и делит текст на слова без цифр, спецсимволов и знаков
    возвращает массив слов исходного текста
    """
    text_result = []
    text = text.lower()
    for char in text:
        if char.isalpha() or char.isspace():
            text_result.append(char)

    text_result = str(''.join(text_result))
    return text_result.split()

text1 = input('Введите первый текст: ')#'яблоко, гРуша, вода, мандарин'
text2 = input('Введите второй текст: ')#'груШа, крыша, я, ты, банан, вОда'

words_text1 = split_text(text1)
words_text2 = split_text(text2)

#ищем одинаковые слова в исходных текстах
same_words = []
for i in range(len(words_text1)):
    for j in range(len(words_text2)):
        if words_text1[i] == words_text2[j]:
            same_words.append(words_text1[i])

print(same_words)