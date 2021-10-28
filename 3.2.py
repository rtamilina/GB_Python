def my_func(name, surname, year, city, email, number):
    result = f'{name} {surname}, {year} года рождения, город проживания {city}, почта: {email}, телефон {number}'
    return result


print(my_func(name='Рита', surname='Тамилина', year=1990, city='Москва', email='rrrr@gmail.com', number='7-777-777'))
