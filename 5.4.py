data = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('text_4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_list.append(data[i[0]] + ' ' + i[1])
    print(new_list)

with open('text_8.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_list)
