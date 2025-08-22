from django.db import models

class OriginalTitle(models.Model):
    title = models.CharField(max_length=128)

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    original_title = models.OneToOneField(
        OriginalTitle,
        on_delete=models.SET_NULL,
        null=True
    )