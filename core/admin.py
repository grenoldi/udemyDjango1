from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


class ClientAdmin(admin.ModelAdmin):
    list_display = (Client.__str__, 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
