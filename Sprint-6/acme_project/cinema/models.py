from django.db import models

class BaseModel(models.Model):
    """
    Абстрактная модель. 
    Добавляет к модели дату создания и последнего изменения. 
    """
    # Параметр auto_now_add=True означает
    # "при СОЗДАНИИ записи автоматически записывать в это поле текущее время".
    created_at = models.DateTimeField(auto_now_add=True)
    # Параметр auto_now=True означает
    # "при ИЗМЕНЕНИИ записи автоматически записывать в это поле текущее время".
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    # С помощью необязательного внутреннего класса Meta можно добавить
    # к модели дополнительные настройки. 
    class Meta:
        # Эта строка объявляет модель абстрактной:
        abstract = True 

class OriginalTitle(BaseModel):
    title = models.CharField(max_length=128)

class ProductType(BaseModel):
    title = models.CharField(max_length=128)

class VideoProduct(BaseModel):
    title = models.CharField(max_length=128)
    original_title = models.OneToOneField(
        OriginalTitle,
        on_delete=models.SET_NULL,
        null=True
    )

    directors = models.ManyToManyField(
        'Director',
        through='Partnership'
    )

    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
    )

class Director(BaseModel):
    full_name = models.CharField(max_length=128)

class Partnership(BaseModel):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    video_product = models.ForeignKey(VideoProduct, on_delete=models.CASCADE)

    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=300)
