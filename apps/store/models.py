from django.db import models


# ------------------------------------------------------------------------------------->
# Model Store


class Store(models.Model):
    store = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=100, null=True)
    direction = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    phone2 = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Store'

    def __str__(self):
        return "%s %s" % (self.store, self.branch)


# ------------------------------------------------------------------------------------->

