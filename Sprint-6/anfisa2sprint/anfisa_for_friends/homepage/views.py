# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        # Делаем запрос, объединяя два условия
        # через Q-объекты и оператор AND:
        Q(is_published=True) & Q(is_on_main=True)
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context) 