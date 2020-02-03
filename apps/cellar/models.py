from django.db import models
from apps.store.models import Store
from apps.staff.models import Staff
from apps.product.models import Product


# ------------------------------------------------------------------------------------>
# Model Cellar


class Cellar(models.Model):
    name = models.CharField(max_length=100, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    direction = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Cellar'
        verbose_name_plural = 'Cellar'

    def __str__(self):
        return self .name


# ------------------------------------------------------------------------------------>
# Model Inventory


class Inventory(models.Model):
    cellar = models.ForeignKey(Cellar, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    available = models.IntegerField()

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return self.cellar


# ------------------------------------------------------------------------------------>
# Model TypeMovement

class TypeMovement(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'TypeMovement'
        verbose_name_plural = 'TypeMovement'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model Movement


class Movement(models.Model):
    typeMovement = models.ForeignKey(TypeMovement, on_delete=models.CASCADE, null=True)
    requested = models.ForeignKey(Staff, related_name='requested', on_delete=models.CASCADE, null=True)
    approved = models.ForeignKey(Staff, related_name='approved', on_delete=models.CASCADE, null=True)
    dateRequest = models.DateField(null=True)
    dateApproved = models.DateField(null=True)
    cellarEntrance = models.ForeignKey(Cellar, related_name='cellar_entrance', on_delete=models.CASCADE, null=True)
    CellarExit = models.ForeignKey(Cellar, related_name='cellar_exit', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Movement'
        verbose_name_plural = 'Movement'

    def __str__(self):
        return "%s %s" % (self.dateRequest, self.requested)


# ------------------------------------------------------------------------------------>
# Model DetailMovement


class DetailMovement(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'DetailMovement'
        verbose_name_plural = 'DetailMovement'

    def __str__(self):
        return "%s %s" % (self.movement, self.product)
