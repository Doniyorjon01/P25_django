from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE, TextField, DecimalField, ImageField


class Category(models.Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    # description = TextField()
    image = ImageField(upload_to='products/')
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    name = CharField(max_length=255)
    headshot = models.ImageField(null=True, blank=True, upload_to="hero_headshots/")

    class Meta:
        db_table = "product_user"
