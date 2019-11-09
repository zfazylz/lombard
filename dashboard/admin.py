from django.contrib import admin

from .models import *
from django.forms import TextInput, Textarea, NumberInput


@admin.register(LombardBranch)
class LombardBranchAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ['name', 'percent']


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'storage', 'lombard_branch', 'price', 'category', 'tariff', 'placed_at', 'buyout_date',
                    'buyout_price_name']
    readonly_fields = ('buyout_price_name',)

    def buyout_price_name(self, obj):
        return "%d" % (obj.buyout_price())

    buyout_price_name.short_description = 'Стоимость выкупа'

    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': '20'})},
        # models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }