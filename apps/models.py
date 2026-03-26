from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import Model, CharField, ForeignKey, CASCADE, DecimalField, IntegerField, ImageField, Q, F, \
    ManyToManyField, JSONField, EmailField, TextChoices
from django.db.models.constraints import CheckConstraint
from django.db.models.fields import PositiveIntegerField, DateTimeField, SmallIntegerField, PositiveSmallIntegerField, \
    TextField
from django.utils.timezone import now


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(null=False, blank=False, max_length=100)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    description = TextField()
    specification = JSONField(default=dict)
    price = DecimalField(max_digits=10, decimal_places=2)
    discount = PositiveSmallIntegerField(default=0, help_text='Chegirma (% foizda)')
    shipping_cost = PositiveIntegerField(default=0)
    like_count = PositiveIntegerField(default=0)
    tags = ManyToManyField('apps.Tag', blank=True)

    quantity = PositiveIntegerField(default=0)
    created_at = DateTimeField(auto_now=True)

    @property
    def current_price(self):
        return self.price - self.price * self.discount / 100

    @property
    def is_new(self):
        return now().date() - self.created_at.date() < timedelta(days=3)

    @property
    def is_in_stock(self):
        return self.quantity > 0

    class Meta:
        constraints = [
            CheckConstraint(condition=Q(discount__lte=100), name='check_product_price',
                            violation_error_message="Chegirma foizda (0-100 oraliqda bolishi kerak)")
        ]


class ProductImage(Model):
    image = ImageField(upload_to='products/%Y/%m/%d')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')


class Review(Model):
    title = CharField(max_length=255)
    comment = TextField()
    product = ForeignKey('apps.Product', CASCADE, related_name='reviews')
    author = ForeignKey('auth.User', CASCADE, related_name='reviews')
    created_at = DateTimeField(auto_now=True)
