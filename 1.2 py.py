while True:
    sec = int(input('Сколько секунд'))
    hour = sec // 3600
    minute = sec % 3600 // 60
    seconds = sec % 3600 % 60

    print(f'Количество часов, минут, секунд: {hour}:{minute}:{seconds}')
