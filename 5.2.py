with open('text_4.txt', 'r') as f:
    lines = 0
    for line in f:
        lines += 1

print(f'Строк в файле: {lines}')

with open('text_4.txt', 'r') as f:
    for line in f.readlines():
        words = len(line.split(' '))
        print(f"Слов в строке {line}: {words}")
