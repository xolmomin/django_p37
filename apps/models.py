from django.db.models import CharField, Model, ForeignKey, CASCADE
from django.db.models.fields import IntegerField, TextField, BooleanField


class Category(Model):
    name = CharField(max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    description = TextField()
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.name
