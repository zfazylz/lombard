from django.db import models
from datetime import datetime
from django.utils.timezone import now

class LombardBranch(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return "Филиал %s" % self.name


class Storage(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Место храниения'
        verbose_name_plural = 'Места Хранения'

    def __str__(self):
        return "Место хранения %s" % self.name


class Tariff(models.Model):
    name = models.CharField('Название', max_length=100)
    percent = models.FloatField('Процентная ставка в день')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return "Тариф %s" % self.name


class ItemCategory(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Категория имуществ'
        verbose_name_plural = 'Категории имуществ'

    def __str__(self):
        return "Категория %s" % self.name


class Item(models.Model):
    name = models.CharField('Навзвание', max_length=100)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, blank=True)
    lombard_branch = models.ForeignKey(LombardBranch, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField('Цена')
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True, blank=True)
    placed_at = models.DateField('Дата от', default=now)
    buyout_date = models.DateField('Дата до', blank=True, null=True)
    finished = models.BooleanField('Выкуплен?', default=False)

    def buyout_price(self):
        days = (self.buyout_date - self.placed_at).days
        price = self.price * (1 + pow(1 + self.tariff.percent / 100, days))
        return int(price)

    def __str__(self):
        return "Имущество %s" % self.name

    class Meta:
        verbose_name = 'Залоговое имущество'
        verbose_name_plural = 'Залоговые имущества'
