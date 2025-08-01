# 1. Перед вами код модуля, который подсчитывает репутацию персонажа после поединка, но качество кода в этом модуле оставляет желать лучшего.
# Ваша задача — навести порядок в этом коде:
#     проаннотировать переменные и функции,
#     привести код в соответствие с PEP8.

# Подсказка
# 2. Проаннотируйте код в файле main.py проекта character_creation_module. Результат скопируйте в тренажёр и нажмите кнопку «Проверить».
# Обратите внимание, что вызов функции main() в тренажёре не нужен, поэтому не нужно его копировать.
# Когда проверка пройдёт успешно, отправьте код на GitHub.

from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == "warrior":
        return f"{char_name} нанёс противнику урон, равный {5 + randint(3, 5)}"
    elif char_class == "mage":
        return f"{char_name} нанёс противнику урон, равный {5 + randint(5, 10)}"
    elif char_class == "healer":
        return f"{char_name} нанёс противнику урон, равный {5 + randint(-3, -1)}"
    return ""


def defence(char_name: str, char_class: str) -> str:
    if char_class == "warrior":
        return f"{char_name} блокировал {10 + randint(5, 10)} ед. урона"
    elif char_class == "mage":
        return f"{char_name} блокировал {10 + randint(-2, 2)} ед. урона"
    elif char_class == "healer":
        return f"{char_name} блокировал {10 + randint(2, 5)} ед. урона"
    return ""


def special(char_name: str, char_class: str) -> str:
    if char_class == "warrior":
        return f"{char_name} применил специальное умение «Выносливость {80 + 25}»"
    elif char_class == "mage":
        return f"{char_name} применил специальное умение «Атака {5 + 40}»"
    elif char_class == "healer":
        return f"{char_name} применил специальное умение «Защита {10 + 30}»"
    return ""


def start_training(char_name: str, char_class: str) -> str:
    if char_class == "warrior":
        print(f"{char_name}, ты Воитель — великий мастер ближнего боя.")
    elif char_class == "mage":
        print(f"{char_name}, ты Маг — превосходный укротитель стихий.")
    elif char_class == "healer":
        print(f"{char_name}, ты Лекарь — чародей, способный исцелять раны.")

    print("Потренируйся управлять своими навыками.")
    print(
        "Введи одну из команд: attack — чтобы атаковать противника, "
        "defence — чтобы блокировать атаку противника или "
        "special — чтобы использовать свою суперсилу."
    )
    print("Если не хочешь тренироваться, введи команду skip.")

    cmd: str = ""
    while cmd != "skip":
        cmd = input("Введи команду: ")
        if cmd == "attack":
            print(attack(char_name, char_class))
        elif cmd == "defence":
            print(defence(char_name, char_class))
        elif cmd == "special":
            print(special(char_name, char_class))
    return "Тренировка окончена."


def choice_char_class() -> str:
    approve_choice: str = ""
    char_class: str = ""

    while approve_choice != "y":
        char_class = input(
            "Введи название персонажа, за которого хочешь играть: "
            "Воитель — warrior, Маг — mage, Лекарь — healer: "
        ).lower()

        if char_class == "warrior":
            print(
                "Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный."
            )
        elif char_class == "mage":
            print("Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.")
        elif char_class == "healer":
            print(
                "Лекарь — могущественный заклинатель. Черпает силы из природы, веры и духов."
            )

        approve_choice = input(
            "Нажми (Y), чтобы подтвердить выбор, "
            "или любую другую кнопку, чтобы выбрать другого персонажа: "
        ).lower()

    return char_class


def main() -> None:
    print("Приветствую тебя, искатель приключений!")
    print("Прежде чем начать игру...")
    char_name: str = input("...назови себя: ")
    print(
        f"Здравствуй, {char_name}! "
        "Сейчас твоя выносливость — 80, атака — 5 и защита — 10."
    )
    print("Ты можешь выбрать один из трёх путей силы:")
    print("Воитель, Маг, Лекарь")
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
