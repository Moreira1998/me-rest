from django.db import models
from apps.product.models import Product, Price


# ------------------------------------------------------------------------------------>
# Model Supplier


class Supplier(models.Model):
    idSupplier = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Supplier'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model TypeBuy


class TypeBuy(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'TypeBuy'
        verbose_name_plural = 'TypeBuy'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model Buy


class Buy(models.Model):
    idBuy = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    typeBuy = models.ForeignKey(TypeBuy, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Buy'
        verbose_name_plural = 'Buy'

    def __str__(self):
        return self.idBuy


# ------------------------------------------------------------------------------------>
# Model DetailBuy


class DetailBuy(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'DetailBuy'
        verbose_name_plural = 'DetailBuy'

    def __str__(self):
        return self.product
