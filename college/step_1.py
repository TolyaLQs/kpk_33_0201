import random


moods = ['веселый', 'серьезный','озадаченый', 'активный']

f = open('nemes.txt', 'r', encoding='utf-8')

file_content = f.readlines()


for idx, element in enumerate(file_content):
        file_content[idx] = element.replace("\n", "")





for name in file_content:
    phrase = f'{name} сегодня {random.sample(moods,1)[0]}'
    print(phrase)