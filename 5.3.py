with open('text_3.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n')
    print(data)
    salary = []
    low_salary = []
for i in data:
    i = i.split()
    if float(i[1]) < 20000:
        low_salary.append(i)
    salary.append(i[1])
aver_salary = sum(map(float, salary)) / len(salary)
print(f'Оклад меньше 20000: {low_salary}, средний оклад: {aver_salary}')
