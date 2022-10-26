#Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом,
# что ключ — название банка, значение — процент. Напишите программу, в результате которой будет сформирован
# список deposit значений — накопленные средства за год вклада в каждом из банков. На вход программы с клавиатуры
# вводится сумма money, которую человек планирует положить под проценты.

# Создаем словарь per_cent с распределением процентных ставок по вкладам в различных банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Создаем переменную money, принимающую на вход сумму, которую человек планирует положить под проценты
money = int(input('Введите сумму: '))

# Создаем и заполняем список deposit для хранения данных о накопленных средствах за год вклада в каждом из банков
deposit = []
for value in per_cent.values():
    deposit.append(int(money*value/100))

# Находим максимальное значение в списке deposit
max_income = max(deposit)
# Выводим на экран информацию о максимальной сумме, которую может заработать пользователь
print(f'Максимальная сумма, которую вы можете заработать {max_income}')