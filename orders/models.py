from django.contrib.auth.models import User
from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)

    # Many to one, один-до-багатьох (в одного user може бути багато замовленнь)
    # on_delete=CASCADE означає, що якщо User видаляється, всі пов'язані з ним SalesOrder також будуть видалені.
    # null=True якщо раніше були створені замовлення(моделі), то їм присвоюється null замість user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
