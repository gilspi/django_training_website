from tabnanny import verbose
from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(verbose_name="price", max_length=20)
    pc_desc = models.CharField(verbose_name="description", max_length=200)

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = "Prices"
        verbose_name_plural = "Prices"


class PriceTable(models.Model):
    pt_title = models.CharField(verbose_name="Title", max_length=200)
    pt_old_price = models.CharField(verbose_name="Old price", max_length=200)
    pt_new_price = models.CharField(verbose_name="New price", max_length=200)

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Table"
