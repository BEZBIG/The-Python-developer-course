# 2. Добавьте в класс Quest два метода:
#     accept_quest() — чтобы игрок мог взять квест;
#     pass_quest() — чтобы игрок мог завершить квест.
# Чтобы зафиксировать время начала и завершения квеста, в конструктор класса Quest добавьте свойства start_time и end_time.
# Определите их начальные значения как None.
# В метод accept_quest() в свойство start_time запишите текущее время. Метод должен вернуть фразу 'Начало "{название_квеста}" положено.'
# В метод pass_quest() в свойство end_time тоже запишите текущее время.
# Также в этом методе объявите переменную completion_time и посчитайте в ней разницу между временем завершения и начала квеста.
# Метод должен вернуть фразу 'Квест "{название_квеста}" окончен. Время выполнения квеста: {разница_между_завершением_и_началом_квеста}'.
# Также добавьте в оба метода ограничения:
#     Для accept_quest(): если при вызове метода для объекта класса в свойстве end_time уже записано значение, то нужно вернуть строку 'С этим испытанием вы уже справились.'.
#     Игрок уже выполнил квест, вызвать его повторно нельзя.
#     Для pass_quest(): если при вызове метода у объекта квеста свойство start_time равно None, должна вернуться строка 'Нельзя завершить то, что не имеет начала!'.
#     Нельзя завершить квест, который игрок не начал выполнять.

# Подсказка
# Для свойств конструктора класса start_time и end_time поставьте None как начальное значение.
# Методы accept_quest() и pass_quest() должны принимать единственный параметр — self.
# Для записи текущего времени используйте метод now() модуля datetime.
# Следите за пунктуацией и орфографией в принтах.


import datetime as dt
import time


class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time is not None:
            return "С этим испытанием вы уже справились."
        self.start_time = dt.datetime.now()
        return f'Начало "{self.name}" положено.'

    def pass_quest(self):
        if self.start_time is None:
            return "Нельзя завершить то, что не имеет начала!"
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (
            f'Квест "{self.name}" окончен. Время выполнения квеста: {completion_time}'
        )


quest_name = "Сбор пиксельники"
quest_goal = "Соберите 12 ягод пиксельники."
quest_description = """
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники."""


new_quest = Quest(quest_name, quest_description, quest_goal)


print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
