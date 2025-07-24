# 5. Код стал большим, и в нём стали повторяться функциональные блоки. Чтобы избежать повторов — соберите код в функцию.
# Функция должна называться get_days_to_birthday и принимать параметр date_birthday:
# def get_days_to_birthday(date_birthday)
#     Функция get_days_to_birthday() получает на вход дату рождения определённого человека.
#     Функция get_days_to_birthday() не должна ничего печатать, она должна возвращать количество дней, оставшихся до дня рождения в этом году.
# Уберите из кода print() и добавьте return <количество_дней_до_дня_рождения>.
# Вызовите функцию два раза: в первом вызове передайте в функцию день рождения Леры, во втором — день рождения Максима. Напечатайте результат каждого вызова.

# Подсказка
# Вместо двух одинаковых фрагментов кода, обрабатывающих дни рождения Максима и Леры, в теле функции должен остаться лишь один, универсальный: он будет обрабатывать любую дату, полученную при вызове функции.
# Результат работы функции возвращайте с помощью return.
# Вызов функции и печать  результата для дня рождения Максима может выглядеть так…
# print(get_days_to_birthday(maxim_birthday))
# …или так:
# max_days = get_days_to_birthday(maxim_birthday)
# print(max_days)


import datetime as dt


def get_days_to_birthday(date_birthday):

    today = dt.date.today()
    today_year = today.year
    days_to_birthday = date_birthday.replace(year=today_year) - today

    return days_to_birthday


lera_birthday = dt.date(2015, 5, 16)
maxim_birthday = dt.date(2011, 12, 16)

print(get_days_to_birthday(lera_birthday))
print(get_days_to_birthday(maxim_birthday))
