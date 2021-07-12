from django.db import models


# Create your models here.
class Order(models.Model):  # Создание модели приложения
    order_dt = models.DateTimeField(auto_now=True)  # Создание поля модели приложения
    order_name = models.CharField(max_length=200, verbose_name='Имя')  # Создание поля модели приложения
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')  # Создание поля модели приложения

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'  # Название модели в единственном числе
        verbose_name_plural = 'Заказы'  # Название модели во множественном числе
