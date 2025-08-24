from django.db import models

class OriginalTitle(models.Model):
    title = models.CharField(max_length=128)

class ProductType(models.Model):
    title = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    original_title = models.OneToOneField(
        OriginalTitle,
        on_delete=models.SET_NULL,
        null=True
    )

    directors = models.ManyToManyField(
        'Director'
    )

    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
    )

class Director(models.Model):
    full_name = models.CharField(max_length=128)

class DirectorVideoProduct(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    video_product = models.ForeignKey(VideoProduct, on_delete=models.CASCADE)