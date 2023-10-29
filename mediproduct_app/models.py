from django.db import models

class ProductRequest(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="الاسم الثلاثي")
    phone_number = models.CharField(max_length=15, verbose_name="رقم الجوال")
    country = models.CharField(max_length=50, verbose_name="الدولة")
    address = models.TextField(verbose_name="العنوان")

    def __str__(self):
        return self.full_name