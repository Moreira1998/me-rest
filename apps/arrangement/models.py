from django.db import models

from apps.store.models import Store


# ------------------------------------------------------------------------------------->
# Model Arrangement


class Arrangement(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    ShippingDescription = models.CharField(max_length=100, null=True)
    Store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Arrangement'
        verbose_name_plural = 'Arrangement'

    def __str__(self):
        return self .name


# ------------------------------------------------------------------------------------->
# Model TypeOrder


class TypeOrder(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'TypeOrder'
        verbose_name_plural = 'TypeOrder'

    def __str__(self):
        return self .name


# ------------------------------------------------------------------------------------->
# Model Order


class Order(models.Model):
    typeOrder = models.ForeignKey(TypeOrder, on_delete=models.CASCADE, null=True)
    orderData = models.DateField(null=True)
    deliverData = models.DateField(null=True)
    state = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return self .orderData

# ------------------------------------------------------------------------------------->
# Model Client


class Client(models.Model):
    idClient = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    direction = models.CharField(max_length=100, null=True)
    phone1 = models.CharField(max_length=100, null=True)
    phone2 = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

    def __str__(self):
        return self .idClient


# ------------------------------------------------------------------------------------->
# Model DetailOrder


class DetailOrder(models.Model):
    arrangement = models.ForeignKey(Arrangement, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=True)
    quantity = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

    def __str__(self):
        return self .idClient