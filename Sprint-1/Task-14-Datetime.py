# 1.Импортируйте модуль datetime.
# Один из типов данных, доступных в модуле datetime, называется точно так же, как и сам модуль.
# В результате обращение к этому типу может выглядеть как datetime.datetime(...).
# Это может привести к путанице; чтобы избежать её — при импорте переименуйте модуль.
# Напечатайте в консоль текущую дату и время.

# Подсказка
# Переименование модуля выполняется с помощью ключевого слова as: import имя_модуля as новое_имя.
# Получить актуальное время и дату можно через метод now(), он доступен только для одного типа данных из модуля datetime.

import datetime as dtime

now_date_time = dtime.datetime.now()
print(now_date_time)
