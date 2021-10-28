def my_func(word):
    return word.title()


type_list = input('Введите слова через пробел: ').split()
for words in type_list:
    result = my_func(words)
    print(result)
