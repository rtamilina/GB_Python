data = input('Введите данные: \n').split()

with open('text_1.txt', 'w', encoding='utf-8') as f:
    for i in data:
        f.write(i + '\n')
