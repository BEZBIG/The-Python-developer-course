from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper

# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

admin.site.register(Category, CategoryAdmin) 

# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):  
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)

# Регистрируем новый класс: 
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin 
admin.site.register(IceCream, IceCreamAdmin)
admin.site.empty_value_display = 'Не задано' 