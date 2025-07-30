# 4. У каждого вида птиц есть особые навыки. Например, попугай может повторить сказанную ему фразу, а пингвины умеют плавать со средней скоростью 11 км/ч.
# Для класса Parrot объявите метод repeat(), который в качестве параметра принимает phrase фразу и возвращает строку Попугай {name} говорит: {phrase}.
# Для класса Penguin объявите метод swimming(), который будет возвращать строку: Пингвин {name} плавает со средней скоростью 11 км/ч..

# Подсказка
# Свойства, используемые в методах, вызываются через self, а параметры, передаваемые в метод, нет.


class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f"Размер птицы {self.name} - {self.size}"


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if full:
            return (
                f"Попугай {self.name} — заметная птица, окрас её перьев — {self.color}, а размер — {self.size}."
                f"Интересный факт: попугаи чувствуют ритм, а вовсе не бездумно двигаются под музыку. Если сменить композицию, то и темп движений птицы изменится."
            )
        return super().describe()

    def repeat(self, phrase):
        return f"Попугай {self.name} говорит: {phrase}"


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if full:
            return (
                f"Размер пингвина {self.name} из рода genus — {self.size}."
                f"Интересный факт: однажды группа геологов-разведчиков похитила пингвинье яйцо, и их принялась преследовать вся стая, не пытаясь, впрочем, при этом нападать."
                "Посовещавшись, похитители вернули птицам яйцо, и те отстали."
            )
        return super().describe()

    def swimming(self):
        return f"Пингвин {self.name} плавает со средней скоростью 11 км/ч."


kesha = Parrot("Apa", "средний", "красный")
kowalski = Penguin("Королевский", "большой", "Aptenodytes")
