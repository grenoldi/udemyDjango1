from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=9)
    quantity = models.IntegerField('quantity')

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    name = models.CharField('name', max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    email = models.EmailField('e-mail', max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'
