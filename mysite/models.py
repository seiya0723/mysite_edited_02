from django.db import models
import uuid

from django.db.models.fields.related import ManyToManyField
# Create your models here.


class Shop(models.Model):
    class Meta:
        db_table = "shop"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="販売元", max_length=50)


class Category(models.Model):
    class Meta:
        db_table = "category"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="カテゴリー", max_length=10)


class Products(models.Model):
    class Meta:
        db_table = "product"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        Category, verbose_name="カテゴリー", on_delete=models.PROTECT)
    shop = models.ForeignKey(
        Shop, verbose_name="販売元", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="品名", max_length=30)
    price = models.IntegerField(verbose_name="価格")
