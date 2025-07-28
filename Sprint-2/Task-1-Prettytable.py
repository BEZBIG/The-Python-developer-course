# Проверим на практике, как работает виртуальное окружение. Если venv вашего проекта деактивировано, активируйте его, введите команду:
# # Директория, в которой вы должны находиться ...Dev/first_project.

# # Для Windows:
# source venv/Scripts/activate

# # Для Linux и macOS:
# source venv/bin/activate 
# Протестируем работу виртуального окружения на библиотеке prettytable. Эта библиотека выводит в терминал данные в табличном виде. 
# Установите библиотеку через терминал, используя команду:
# (venv)...$ pip install prettytable 
# По этой команде запустится менеджер пакетов pip, он найдёт, скачает и установит библиотеку prettytable на компьютер, в виртуальное окружение проекта. 
# Служебные файлы prettytable будут сохранены в директории Dev/first_project/venv.

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Name', 'Age', 'City']
table.add_row(['Стёпа', 11, 'Москва'])
table.add_row(['Андрей', 7, 'Ковров'])
table.add_row(['Тоня', 6, 'Минск'])
table.add_row(['Толя', 8, 'Санкт-Петербург'])
table.add_row(['Лера', 5, 'Краснодар'])

print(table)