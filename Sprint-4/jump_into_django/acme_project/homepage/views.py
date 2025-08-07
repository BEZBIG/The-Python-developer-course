from django.shortcuts import render

# Класс HttpResponse нужно импортировать в код из модуля django.http.
from django.http import HttpResponse

# Импортируем загрузчик.
from django.template import loader

def index(request):    
    # Адрес шаблона сохранён в переменную, это не обязательно, но удобно.
    template_name = 'homepage/index.html'
    # Строка, которую надо вывести на страницу, тоже сохранена в переменную.
    title = 'Главная страница ACME'
    promo_product = 'Iron carrot'
    context = {
        # Ключ словаря и имя переменной не обязательно называть одинаково,
        # но обычно это удобнее, чем использовать два разных имени.
        'title': title,
        'promo_product': promo_product,
    }
    # Третьим аргументом в render() передаём словарь context:
    return render(request, template_name, context)
