from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class SalesOrder(models.Model):
    # fields:
    amount = models.IntegerField()
    description = models.CharField(max_length=255)

    # Many to one, багато до одного (в одного user може бути багато замовленнь)
    # on_delete=CASCADE означає, що якщо User видаляється, всі пов'язані з ним SalesOrder також будуть видалені.
    # null=True якщо раніше були створені замовлення(моделі), то їм присвоюється null замість user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Many To many (між замовленнями можуть бути багато продуктів)
    products = models.ManyToManyField(Product)
