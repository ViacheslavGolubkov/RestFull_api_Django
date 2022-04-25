from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    title = models.CharField(verbose_name='Заголовок', max_length=30)
    text = models.TextField(verbose_name='Текст:', blank=True)
    is_public = models.BooleanField(verbose_name='Публичная статья:', default=False)

    def __str__(self):
        return self.title
