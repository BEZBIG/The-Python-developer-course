# 3. Выведите на печать содержимое объекта класса Quest.
# Для этого переопределите метод __str__ в классе Quest. По умолчанию он должен возвращать строку 'Цель квеста {название_квеста} - {цель_квеста}.'.
# При определённых условиях строка должна выглядеть иначе:
#     если квест уже завершён — 'Цель квеста {название_квеста} - {цель_квеста}. Квест завершён.';
#     если квест уже принят на исполнение — 'Цель квеста {название_квеста} - {цель_квеста}. Квест выполняется.'.

# Подсказка
# Метод для печати объекта — __str__.
# Чтобы дополнить исходную строку, используйте конкатенацию.

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
        if self.end_time:

            return "С этим испытанием вы уже справились."
        self.start_time = dt.datetime.now()
        return f'Начало квеста "{self.name}" положено.'

    def pass_quest(self):
        if not self.start_time:
            return "Нельзя завершить то, что не имеет начала!"
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (
            f'Квест "{self.name}" окончен.'
            f" Время выполнения квеста: {completion_time}"
        )

    def __str__(self):
        final_str = f"Цель квеста {self.name} - {self.goal}."
        if self.end_time is not None:
            final_str += " Квест завешен."
        elif self.start_time is not None and self.end_time is None:
            final_str += " Квест выполняется."
        return final_str


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


# Печатаем объекта класса Quest:
print(new_quest)
