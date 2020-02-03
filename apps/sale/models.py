from django.db import models
from apps.product.models import Product, Price
from apps.store.models import Store


# ------------------------------------------------------------------------------------>
# Model TypeBill


class TypeBill(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'TypeBill'
        verbose_name_plural = 'TypeBill'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model TypeSale


class TypeSale(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'TypeSale'
        verbose_name_plural = 'TypeSale'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model Sale


class Sale(models.Model):
    idSale = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    typeSale = models.ForeignKey(TypeSale, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sale'

    def __str__(self):
        return self.idSale


# ------------------------------------------------------------------------------------>
# Model Bill


class Bill(models.Model):
    idBill = models.IntegerField()
    date = models.DateField()
    subTotal = models.FloatField()
    total = models.FloatField()
    payment = models.FloatField()
    change = models.FloatField()
    typeBill = models.ForeignKey(TypeBill, on_delete=models.CASCADE, null=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bill'

    def __str__(self):
        return self.idBill


# ------------------------------------------------------------------------------------>
# Model DetailSale


class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'DetailSale'
        verbose_name_plural = 'DetailSale'

    def __str__(self):
        return self.product


# ------------------------------------------------------------------------------------>

