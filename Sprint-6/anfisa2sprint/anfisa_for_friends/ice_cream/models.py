from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256, help_text='Уникальное название обёртки, не более 256 символов')
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField('Порядок вывода', default=100)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.title 

class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256, help_text='Уникальное название топпинга, не более 256 символов')
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title

class Wrapper(PublishedModel):
    title = models.CharField('Название', max_length=256, help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self):
        return self.title

class IceCream(PublishedModel):
    title = models.CharField('Название', max_length=256, help_text='Уникальное название мороженого, не более 256 символов')
    description = models.TextField('Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        verbose_name='Обертка',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория',
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False)

    output_order = models.PositiveSmallIntegerField('Порядок вывода', default=100)
    price = models.DecimalField(max_digits=5, decimal_places=2) 

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title

