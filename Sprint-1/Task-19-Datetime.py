# 6. Если день рождения в этом году уже прошёл — функция get_days_to_birthday() вернёт отрицательное значение.
# Но все хотят знать, долго ли ждать новых подарков, а не сколько времени прошло после праздника.
# Если date_birthday для текущего года меньше today — значит, день рождения в этому году уже прошёл.
# В этом случае вычислите количество дней, оставшихся до дня рождения, который будет в следующем году.
# Подробности
#     Объекты date поддерживают операции сравнения:
#     print(today > lera_birthday)
#     # Вывод в терминал True

#     print(today == maxim_birthday)
#     # Вывод в терминал: False

#     Большей считается дата, наступившая позже.
#     В коде пригодится ветвление if ... else.

# Подсказка
# Проверьте, прошёл ли уже в этом году день рождения.
# Если не прошёл — функция должна отработать, как и прежде.
# Если прошёл — надо рассчитать, сколько дней до дня рождения, который наступит в будущем году.
# Для этого примените метод replace(): увеличьте значение года на 1. После этого вычислите разность между сегодняшней датой и датой дня рождения в будущем году.

import datetime as dt


def get_days_to_birthday(date_birthday):

    today = dt.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)

    if date_birthday > today:
        days_to_birthday = date_birthday.replace(year=today_year) - today
    else:
        date_birthday = date_birthday.replace(year=today_year + 1)
        days_to_birthday = date_birthday - today

    return days_to_birthday.days


lera_birthday = dt.date(2015, 5, 16)
maxim_birthday = dt.date(2011, 12, 16)

print(get_days_to_birthday(lera_birthday))
print(get_days_to_birthday(maxim_birthday))
