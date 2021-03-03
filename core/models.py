from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=20, null=True, verbose_name="Ваше имя")
    email = models.EmailField(null=True, verbose_name="Ваша почта")
    phone = models.IntegerField(null=True, verbose_name="Ваш номер +7")
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
    def __str__(self):
        return self.name