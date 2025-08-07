from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category>/', views.product_category),
    # Если пришёл запрос к относительному URL catalog/,
    # то запрос из корневого urls.py перенаправляется сюда, 
    # в файл catalog/urls.py;
    # и если в запросе после 'catalog/' ничего нет (пустая строка),
    # будет вызвана view-функция product_list() из файла catalog/views.py
    # Имя для URL лучше задавать такое же, как и имя функции. 
    # Легко запомнить, просто понять:
    path('catalog/', views.product_list, name='product_list'),  
    path('catalog/<int:pk>/', views.product_detail, name='product_detail'),
] 