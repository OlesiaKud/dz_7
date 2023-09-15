# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться 
# в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

def find_rhythm(text, _dict):
    first_s_1 = None
    for word in text:
        s = list(map(lambda letter: letter in _dict, word))
        s_1 = sum(s)
        if first_s_1 is None:
            first_s_1 = s_1
        if s_1 != first_s_1:
            print('Пам парам')
            return
    print('Парам пам-пам')

print('Будем проверять рифму по технологии Винни Пуха.')
print('ОБРАТИТЕ ВНИМАНИЕ!!!\nФраза может состоять из 1 слова, если во фразе несколько слов, то они разделяются ДЕФИСАМИ. \nФразы отделяются друг от друга ПРОБЕЛАМИ.\nПример ввода: пара-ра-рам рам-пам-папам па-ра-па-да') 
my_text = input('Введите ваше стихотворение: ').lower()
text = my_text.split()
rhythm_dict = 'eyuioaуеыаоэяию'
find_rhythm(text, rhythm_dict)
