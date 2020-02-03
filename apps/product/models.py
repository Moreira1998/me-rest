from django.db import models


# ------------------------------------------------------------------------------------>
# Model Category

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self .name


# ------------------------------------------------------------------------------------>
# Model Brand


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model State


class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'State'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model Price


class Price(models.Model):
    purchasePrice = models.FloatField(null=True)
    salePrice = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Price'

    def __str__(self):
        return self.purchasePrice


# ------------------------------------------------------------------------------------>
# Model Product


class Product(models.Model):
    idProduct = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self .name
