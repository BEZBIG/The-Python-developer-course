# Создайте список целых чисел 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 используя списковое включение.
# В качестве источника значений используйте range()

# List Comprehension
numbers = [number**2 for number in range(1, 11)]
print(numbers)

# Магистр Йода состарился и стал совсем плох в речи: он стал менять местами первое и последнее слово фразы.
# Напишите программу, которая сможет привести его фразы в нормальный вид.
# Не создавая нового объекта, поменяйте первое и последнее слово местами.


force_words = ["сила", "пребудет", "с", "тобой", "Да"]
print(id(force_words))
# Место для вашего кода
firt_word = force_words.pop(0)
last_word = force_words.pop(-1)
force_words.insert(0, last_word)
force_words.append(firt_word)

print(force_words)
10
# Убедимся, что это тот же объект, что и в начале программы
11
print(id(force_words))
