from django.db import models
from apps.store.models import Store
from django.contrib.auth.models import User


# ------------------------------------------------------------------------------------>
# Model Role


class Role(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Role'

    def __str__(self):
        return self .name


# ------------------------------------------------------------------------------------->
# Model Staff


class Staff(models.Model):
    idStaff = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    direction = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    phone2 = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(max_length=100, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return self.idStaff


# ------------------------------------------------------------------------------------->
