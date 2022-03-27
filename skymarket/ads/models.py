from django.db import models

from skymarket.users.models import User


class Ad(models.Model):
    image = models.ImageField(upload_to="images/",verbose_name="фото",null=True,blank=True)
    title = models.CharField(max_length=100, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена товара")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Автор объявления")
    created_at = models.DateTimeField(verbose_name="Время создания объявления")
    description = models.CharField(max_length=1000,blank=True,null=True, verbose_name="Описание товара")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = "-created_at"


class Comment(models.Model):
    text = models.CharField(max_length=1000,verbose_name="Комментарий")
    created_at = models.DateTimeField(verbose_name="Время создания комментария")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Автор комментария")
    ad = models.ForeignKey(Ad,on_delete=models.CASCADE,verbose_name="Объявление")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = "-created_at"